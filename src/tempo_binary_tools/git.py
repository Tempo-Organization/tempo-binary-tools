import os
import requests


def get_github_token() -> str | None:
    return os.getenv("GITHUB_TOKEN")


def github_get(url: str, **kwargs) -> requests.Response: # noqa
    headers = kwargs.pop("headers", {})

    token = get_github_token()
    if token:
        headers["Authorization"] = f"Bearer {token}"

    headers["Accept"] = "application/vnd.github+json"

    timeout = kwargs.pop("timeout", 5)  # default once only

    return requests.get(url, headers=headers, timeout=timeout, **kwargs)


def get_commit_short_hash_from_tag(repo_name: str, is_online: bool, tag_name: str = "latest") -> str:
    """
    Returns 7-char commit hash for a GitHub tag.
    Raises exceptions on failure (no silent string errors).
    """

    if not is_online:
        raise RuntimeError(
            "Cannot fetch commit hash while offline.",
        )

    try:
        # Step 1: resolve tag reference
        tag_ref_url = f"https://api.github.com/repos/{repo_name}/git/ref/tags/{tag_name}"
        ref_response = github_get(tag_ref_url, timeout=10)
        ref_response.raise_for_status()

        tag_ref = ref_response.json()

        obj_type = tag_ref.get("object", {}).get("type")
        obj_url = tag_ref.get("object", {}).get("url")

        if not obj_type or not obj_url:
            raise RuntimeError(f"Malformed GitHub response for tag {tag_name}")

        # Case 1: direct commit
        if obj_type == "commit":
            sha = tag_ref["object"]["sha"]
            return sha[:7]

        # Case 2: annotated tag
        tag_object_response = github_get(obj_url, timeout=10)
        tag_object_response.raise_for_status()

        tag_object = tag_object_response.json()

        sha = tag_object.get("object", {}).get("sha")
        if not sha:
            raise RuntimeError("Commit SHA not found in annotated tag response")

        return sha[:7]

    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"GitHub API request failed: {e}") from e

    except KeyError as e:
        raise RuntimeError(f"Unexpected GitHub response structure: {e}") from e

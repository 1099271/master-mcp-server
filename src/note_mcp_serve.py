from typing import Dict, Any, Optional

import httpx

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("masterflow")


async def make_notes_detail_request(note_id: str) -> dict[str, Any] | None:
    """Ask For Note Note Detail By Note ID"""
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                f"http://localhost:8000/openapi/notes/{note_id}"
            )
            response.raise_for_status()
            return response.text
        except httpx.HTTPError:
            return None


@mcp.tool()
async def get_note_details_by_note_id(note_id: str) -> str:
    """Get Alert Details By Note ID
    Args:
        note_id: The ID of the note to get details for
    Returns:
        A string containing the alert details
    """
    note_detail = await make_notes_detail_request(note_id)
    if not note_detail:
        return "无法获取到笔记详情，请确认该笔记是否存在"

    return note_detail


if __name__ == "__main__":
    mcp.run(transport="stdio")

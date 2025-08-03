# This file is part of LangChain.
from langchain_core.messages import ToolMessage, HumanMessage
from langchain_core.messages import AIMessage
from langchain_core.messages import ToolCallMessage
from langchain_core.messages import ToolCall
from langchain_core.messages import ToolCallResponse
from langchain_core.messages import ToolCallResponseMessage
from langchain_core.messages import ToolCallResponseContent

from langchain_core.messages import (
    ToolCallResponseContentItemMetadataValueTypeValueType,
)


def parse_tool_call_response(tool_call_response: ToolCallResponse) -> ToolMessage:
    """Parse a ToolCallResponse into a ToolMessage."""
    tool_call = tool_call_response.tool_call
    content = tool_call_response.content

    # Create a ToolMessage with the content and tool call details
    tool_message = ToolMessage(
        content=content,
        name=tool_call.name,
        id=tool_call.id,
        tool_call_id=tool_call.id,
        artifact=tool_call.artifact if hasattr(tool_call, "artifact") else None,
    )

    return tool_message


def parse_tool_call(tool_call: ToolCall) -> ToolCallMessage:
    """Parse a ToolCall into a ToolCallMessage."""
    tool_call_message = ToolCallMessage(
        content=tool_call.args,
        name=tool_call.name,
        id=tool_call.id,
        tool_call_id=tool_call.id,
        artifact=tool_call.artifact if hasattr(tool_call, "artifact") else None,
    )
    return tool_call_message

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


def parse_ai_message(ai_message: AIMessage) -> AIMessage:
    """Parse an AIMessage into a structured format."""
    tool_calls = (
        [parse_tool_call(tool_call) for tool_call in ai_message.tool_calls]
        if ai_message.tool_calls
        else []
    )

    ai_message_parsed = AIMessage(
        content=ai_message.content,
        additional_kwargs=ai_message.additional_kwargs,
        response_metadata=ai_message.response_metadata,
        id=ai_message.id,
        tool_calls=tool_calls,
        usage_metadata=ai_message.usage_metadata,
    )

    return ai_message_parsed


def parse_human_message(human_message: HumanMessage) -> HumanMessage:
    """Parse a HumanMessage into a structured format."""
    human_message_parsed = HumanMessage(
        content=human_message.content,
        additional_kwargs=human_message.additional_kwargs,
        response_metadata=human_message.response_metadata,
        id=human_message.id,
    )
    return human_message_parsed


def parse_tool_call_response_message(
    tool_call_response_message: ToolCallResponseMessage,
) -> ToolCallResponseMessage:
    """Parse a ToolCallResponseMessage into a structured format."""
    tool_call_response = tool_call_response_message.tool_call_response

    tool_message = parse_tool_call_response(tool_call_response)

    tool_call_response_message_parsed = ToolCallResponseMessage(
        content=tool_message.content,
        name=tool_message.name,
        id=tool_message.id,
        tool_call_id=tool_message.tool_call_id,
        artifact=tool_message.artifact,
    )

    return tool_call_response_message_parsed


def parse_messages(messages):
    """Parse a list of messages into structured format."""
    parsed_messages = []
    for message in messages:
        if isinstance(message, AIMessage):
            parsed_messages.append(parse_ai_message(message))
        elif isinstance(message, HumanMessage):
            parsed_messages.append(parse_human_message(message))
        elif isinstance(message, ToolCallResponseMessage):
            parsed_messages.append(parse_tool_call_response_message(message))
        else:
            parsed_messages.append(message)  # Handle other message types as needed
    return parsed_messages

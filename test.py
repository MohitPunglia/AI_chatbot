{
    "messages": [
        HumanMessage(
            content="What is the latest news in India related to AI ",
            additional_kwargs={},
            response_metadata={},
            id="b9c97836-a04b-4dba-8f47-9871c8614a6a",
        ),
        AIMessage(
            content="",
            additional_kwargs={
                "tool_calls": [
                    {
                        "id": "call_g0bw",
                        "function": {
                            "arguments": '{"query":"latest news in AI"}',
                            "name": "tavily_search_results_json",
                        },
                        "type": "function",
                    }
                ]
            },
            response_metadata={
                "token_usage": {
                    "completion_tokens": 53,
                    "prompt_tokens": 947,
                    "total_tokens": 1000,
                    "completion_time": 0.176793333,
                    "prompt_time": 0.032161947,
                    "queue_time": 0.050550013,
                    "total_time": 0.20895528,
                },
                "model_name": "llama3-70b-8192",
                "system_fingerprint": "fp_dd4ae1c591",
                "finish_reason": "tool_calls",
                "logprobs": None,
            },
            id="run--8183d2c6-39ca-4919-bd9d-53ffa0fe1876-0",
            tool_calls=[
                {
                    "name": "tavily_search_results_json",
                    "args": {"query": "latest news in AI"},
                    "id": "call_g0bw",
                    "type": "tool_call",
                }
            ],
            usage_metadata={
                "input_tokens": 947,
                "output_tokens": 53,
                "total_tokens": 1000,
            },
        ),
        ToolMessage(
            content='[{"url": "https://www.crescendo.ai/news/latest-ai-news-and-updates", "content": "Summary: OpenAI launched \\"Operator,\\" a new AI assistant capable of handling various online tasks, such as ordering groceries and processing ticket purchases."}, {"url": "https://www.nbcnews.com/artificial-intelligence", "content": "The latest news and top stories on artificial intelligence, including AI chatbots like Microsoft\'s ChatGPT, Apple\'s AI Chatbot and Google\'s Bard."}]',
            name="tavily_search_results_json",
            id="e09dc2d6-c225-41fb-8604-a0c66ea9733e",
            tool_call_id="call_g0bw",
            artifact={
                "query": "latest news in AI",
                "follow_up_questions": None,
                "answer": None,
                "images": [],
                "results": [
                    {
                        "url": "https://www.crescendo.ai/news/latest-ai-news-and-updates",
                        "title": "Latest AI Breakthroughs and News: May-June 2025 - Crescendo.ai",
                        "content": 'Summary: OpenAI launched "Operator," a new AI assistant capable of handling various online tasks, such as ordering groceries and processing ticket purchases.',
                        "score": 0.7732339,
                        "raw_content": None,
                    },
                    {
                        "url": "https://www.nbcnews.com/artificial-intelligence",
                        "title": "Artificial intelligence - NBC News",
                        "content": "The latest news and top stories on artificial intelligence, including AI chatbots like Microsoft's ChatGPT, Apple's AI Chatbot and Google's Bard.",
                        "score": 0.769306,
                        "raw_content": None,
                    },
                ],
                "response_time": 2.19,
            },
        ),
        AIMessage(
            content="According to the latest news, OpenAI has launched \"Operator\", a new AI assistant capable of handling various online, such as ordering groceries and processing ticket purchases. Additionally, there are ongoing developments in AI chatbots, with Microsoft's ChatGPT, and Google's Bard.",
            additional_kwargs={},
            response_metadata={
                "token_usage": {
                    "completion_tokens": 56,
                    "prompt_tokens": 1122,
                    "total_tokens": 1178,
                    "completion_time": 0.226801689,
                    "prompt_time": 0.038272468,
                    "queue_time": 0.064210402,
                    "total_time": 0.265074157,
                },
                "model_name": "llama3-70b-8192",
                "system_fingerprint": "fp_dd4ae1c591",
                "finish_reason": "stop",
                "logprobs": None,
            },
            id="run--d5f72e23-9263-4a83-a996-ea9d0fccc938-0",
            usage_metadata={
                "input_tokens": 1122,
                "output_tokens": 56,
                "total_tokens": 1178,
            },
        ),
    ]
}

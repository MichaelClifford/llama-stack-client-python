# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..token_log_probs import TokenLogProbs
from .completion_message import CompletionMessage

__all__ = ["ChatCompletionResponse"]


class ChatCompletionResponse(BaseModel):
    completion_message: CompletionMessage
    """The complete response message"""

    logprobs: Optional[List[TokenLogProbs]] = None
    """Optional log probabilities for generated tokens"""

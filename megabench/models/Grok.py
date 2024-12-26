"""Grok VL.
Works with either the OpenAI or Anthropic APIs: we choose the Anthropic API.
"""
import anthropic
from models.Claude import Claude

class Grok(Claude):
    def make_client(self):
        return anthropic.Anthropic(
            api_key=self.api_key, base_url="https://api.x.ai", max_retries=5
        )
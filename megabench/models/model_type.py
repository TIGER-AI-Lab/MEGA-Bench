import dataclasses
from enum import Enum
import functools
import os
from utils import lazy_import


@dataclasses.dataclass(frozen=True)
class ModelClassContainer:
    module_name: str
    class_name: str

    @functools.cached_property
    def impl(self):
        return lazy_import(self.module_name, self.class_name)()


class ModelClass(ModelClassContainer, Enum):
    OpenAI = ("models.openai", "OpenAI")
    Claude = ("models.claude", "Claude")
    Gemini = ("models.gemini", "Gemini")
    Gemma = ("models.gemma", "Gemma")
    Qwen2VL = ("models.qwen2_vl", "Qwen2VL")
    InternVL = ("models.internvl", "InternVL")
    LlavaOV = ("models.llava_ov", "LlavaOV")
    Pixtral = ("models.pixtral", "Pixtral")
    Phi3v = ("models.phi3v", "Phi3v")
    Grok = ("models.grok", "Grok")
    DeepSeekVL2 = ("models.deepseek_vl2", "DeepSeekVL2")
    Virgo = ("models.virgo", "Virgo")
    Llama4 = ("models.llama4", "Llama4")
    KimiVL = ("models.kimi_vl", "KimiVL")
    GroundTruthOracle = ("models.ground_truth_oracle", "GroundTruthOracle")

@dataclasses.dataclass(frozen=True)
class MaxImagesPerApiCallConfig:
    max_num_image: int
    total_demo_video_frames: int


@dataclasses.dataclass(frozen=True)
class ModelTypeContainer:
    key: str
    model_name: str
    api_key: str
    constructor: type
    max_images_per_api_call: MaxImagesPerApiCallConfig = dataclasses.field(
        default=MaxImagesPerApiCallConfig(64, 8)
    )
    system_message: str | None = dataclasses.field(default=None)


class ModelType(ModelTypeContainer, Enum):

    GPT_4O_MINI = ("gpt_mini", "gpt-4o-mini", "OPENAI_API_KEY", ModelClass.OpenAI)
    GPT_4 = ("gpt-4", "gpt-4-0613", "OPENAI_API_KEY", ModelClass.OpenAI)
    GPT_4O_0513 = (
        "gpt-4o-0513",
        "gpt-4o-2024-05-13",
        "OPENAI_API_KEY",
        ModelClass.OpenAI,
    )
    GPT_4O_0806 = (
        "gpt-4o_0806",
        "gpt-4o-2024-08-06",
        "OPENAI_API_KEY",
        ModelClass.OpenAI,
    )
    CLAUDE_3_HAIKU = (
        "claude_3_haiku",
        "claude-3-haiku-20240307",
        "ANTHROPIC_API_KEY",
        ModelClass.Claude,
    )
    CLAUDE_3_5_SONNET = (
        "claude_3_5_sonnet",
        "claude-3-5-sonnet-20240620",
        "ANTHROPIC_API_KEY",
        ModelClass.Claude,
    )
    CLAUDE_3_OPUS = (
        "claude_3_opus",
        "claude-3-opus-20240229",
        "ANTHROPIC_API_KEY",
        ModelClass.Claude,
    )
    GEMINI_FLASH = (
        "gemini_flash",
        "gemini-1.5-flash-001",
        "GEMINI_API_KEY",
        ModelClass.Gemini,
        MaxImagesPerApiCallConfig(
            max_num_image=128,
            total_demo_video_frames=16,
        ),
    )
    GEMINI_FLASH_002 = (
        "gemini_flash",
        "gemini-1.5-flash-002",
        "GEMINI_API_KEY",
        ModelClass.Gemini,
        MaxImagesPerApiCallConfig(
            max_num_image=128,
            total_demo_video_frames=16,
        ),
    )
    GEMINI_PRO = (
        "gemini_pro",
        "gemini-1.5-pro-001",
        "GEMINI_API_KEY",
        ModelClass.Gemini,
    )
    GEMINI_PRO_002 = (
        "gemini_pro",
        "gemini-1.5-pro-002",
        "GEMINI_API_KEY",
        ModelClass.Gemini,
        MaxImagesPerApiCallConfig(
            max_num_image=128,
            total_demo_video_frames=16,
        ),
    )
    GEMINI_THINKING = (
        "gemini_thinking",
        "gemini-2.0-flash-thinking-exp-1219",
        "GEMINI_API_KEY",
        ModelClass.Gemini,
        MaxImagesPerApiCallConfig(
            max_num_image=100,
            total_demo_video_frames=12,
        ),
    )
    GEMINI_EXP_1206 = (
        "gemini_exp_1206",
        "gemini-exp-1206",
        "GEMINI_API_KEY",
        ModelClass.Gemini,
        MaxImagesPerApiCallConfig(
            max_num_image=128,
            total_demo_video_frames=16,
        ),
    )
    GEMINI_FLASH_2_0_EXP = (
        "gemini_flash_2.0_exp",
        "gemini-2.0-flash-exp",
        "GEMINI_API_KEY",
        ModelClass.Gemini,
        MaxImagesPerApiCallConfig(
            max_num_image=128,
            total_demo_video_frames=16,
        ),
    )
    GEMINI_2_5_PRO_EXP_03_25 = (
        "gemini_2_5_pro_exp_03_25",
        "gemini-2.5-pro-exp-03-25",
        "GEMINI_API_KEY",
        ModelClass.Gemini,
        MaxImagesPerApiCallConfig(
            max_num_image=128,
            total_demo_video_frames=16,
        ),
    )
    GEMMA_3_4B = (
        "gemma_3_4b",
        "google/gemma-3-4b-it",
        "",
        ModelClass.Gemma,
        MaxImagesPerApiCallConfig(
            max_num_image=24,
            total_demo_video_frames=2,
        ),
    )
    GEMMA_3_12B = (
        "gemma_3_12b",
        "google/gemma-3-12b-it",
        "",
        ModelClass.Gemma,
        MaxImagesPerApiCallConfig(
            max_num_image=24,
            total_demo_video_frames=2,
        ),
    )
    GEMMA_3_27B = (
        "gemma_3_27b",
        "google/gemma-3-27b-it",
        "",
        ModelClass.Gemma,
        MaxImagesPerApiCallConfig(
            max_num_image=24,
            total_demo_video_frames=2,
        ),
    )
    QWEN2_VL_72B = (
        "Qwen2_VL_72B",
        "Qwen/Qwen2-VL-72B-Instruct",
        "",
        ModelClass.Qwen2VL,
        MaxImagesPerApiCallConfig(max_num_image=24, total_demo_video_frames=2),
    )
    QWEN2_VL_7B = (
        "Qwen2_VL_7B",
        "Qwen/Qwen2-VL-7B-Instruct",
        "",
        ModelClass.Qwen2VL,
        MaxImagesPerApiCallConfig(max_num_image=18, total_demo_video_frames=2),
    )
    QWEN2_VL_2B = (
        "Qwen2_VL_2B",
        "Qwen/Qwen2-VL-2B-Instruct",
        "",
        ModelClass.Qwen2VL,
        MaxImagesPerApiCallConfig(max_num_image=16, total_demo_video_frames=2),
    )
    QVQ_72B_PREVIEW = (
        "QVQ_72B_Preview",
        "Qwen/QVQ-72B-Preview",
        "",
        ModelClass.Qwen2VL,
        MaxImagesPerApiCallConfig(
            max_num_image=24,
            total_demo_video_frames=2,
        ),
    )
    INTERNVL2_LLAMA3_76B = (
        "InternVL2-Llama3-76B",
        "OpenGVLab/InternVL2-Llama3-76B",
        "",
        ModelClass.InternVL,
        MaxImagesPerApiCallConfig(max_num_image=24, total_demo_video_frames=2),
    )
    INTERNVL2_8B = (
        "InternVL2-8B",
        "OpenGVLab/InternVL2-8B",
        "",
        ModelClass.InternVL,
        MaxImagesPerApiCallConfig(max_num_image=18, total_demo_video_frames=2),
    )
    INTERNVL3_78B = (
        "InternVL3-78B",
        "OpenGVLab/InternVL3-78B",
        "",
        ModelClass.InternVL,
        MaxImagesPerApiCallConfig(max_num_image=24, total_demo_video_frames=2),
    )
    INTERNVL3_38B = (
        "InternVL3-38B",
        "OpenGVLab/InternVL3-38B",
        "",
        ModelClass.InternVL,
        MaxImagesPerApiCallConfig(max_num_image=18, total_demo_video_frames=2),
    )
    INTERNVL3_14B = (
        "InternVL3-14B",
        "OpenGVLab/InternVL3-14B",
        "",
        ModelClass.InternVL,
        MaxImagesPerApiCallConfig(max_num_image=18, total_demo_video_frames=2),
    )
    INTERNVL3_9B = (
        "InternVL3-9B",
        "OpenGVLab/InternVL3-9B",
        "",
        ModelClass.InternVL,
        MaxImagesPerApiCallConfig(max_num_image=18, total_demo_video_frames=2),
    )
    INTERNVL3_8B = (
        "InternVL3-8B",
        "OpenGVLab/InternVL3-8B",
        "",
        ModelClass.InternVL,
        MaxImagesPerApiCallConfig(max_num_image=18, total_demo_video_frames=2),
    )
    LLAVA_ONEVISION_72B = (
        "Llava_OneVision_72B",
        "lmms-lab/llava-onevision-qwen2-72b-ov-chat",
        "",
        ModelClass.LlavaOV,
        MaxImagesPerApiCallConfig(
            max_num_image=28,
            total_demo_video_frames=4,
        ),
    )
    LLAVA_ONEVISION_7B = (
        "Llava_OneVision_7B",
        "lmms-lab/llava-onevision-qwen2-7b-ov",
        "",
        ModelClass.LlavaOV,
        MaxImagesPerApiCallConfig(
            max_num_image=20,
            total_demo_video_frames=4,
        ),
    )
    PIXTRAL_12B = (
        "Pixtral-12B",
        "mistralai/Pixtral-12B-2409",
        "",
        ModelClass.Pixtral,
        MaxImagesPerApiCallConfig(
            max_num_image=48,
            total_demo_video_frames=6,
        ),
    )
    PHI_3_5_VISION = (
        "Phi_3_5_vision",
        "microsoft/Phi-3.5-vision-instruct",
        "",
        ModelClass.Phi3v,
        MaxImagesPerApiCallConfig(
            max_num_image=16,
            total_demo_video_frames=2,
        ),
    )

    PHI_4_MULTIMODAL = (
        "Phi_4_multimodal",
        "microsoft/Phi-4-multimodal-instruct",
        "",
        ModelClass.Phi3v,
        MaxImagesPerApiCallConfig(
            max_num_image=16,
            total_demo_video_frames=2,
        ),
    )
    # This Grok model seems to use many tokens per image.
    GROK_2_VISION_1212 = (
        "grok-2-vision",
        "grok-2-vision-1212",
        "XAI_API_KEY",
        ModelClass.Grok,
        MaxImagesPerApiCallConfig(
            max_num_image=16,
            total_demo_video_frames=2,
        ),
    )
    DEEPSEEK_VL2_TINY = (
        "DeepSeekVL2_Tiny",
        "deepseek-ai/deepseek-vl2-tiny",
        "",
        ModelClass.DeepSeekVL2,
        MaxImagesPerApiCallConfig(
            max_num_image=10,
            total_demo_video_frames=2,
        ),
    )
    DEEPSEEK_VL2_SMALL = (
        "DeepSeekVL2_Small",
        "deepseek-ai/deepseek-vl2-small",
        "",
        ModelClass.DeepSeekVL2,
        MaxImagesPerApiCallConfig(
            max_num_image=10,
            total_demo_video_frames=2,
        ),
    )
    DEEPSEEK_VL2 = (
        "DeepSeekVL2",
        "deepseek-ai/deepseek-vl2",
        "",
        ModelClass.DeepSeekVL2,
        MaxImagesPerApiCallConfig(
            max_num_image=16,
            total_demo_video_frames=2,
        ),
    )
    LLAMA_4_SCOUT_17B = (
        "Llama_4_scout_17b",
        "meta-llama/Llama-4-Scout-17B-16E-Instruct",
        "",
        ModelClass.Llama4,
        MaxImagesPerApiCallConfig(max_num_image=10, total_demo_video_frames=2),
    )
    KIMI_VL_A3B_THINKING = (
        "KimiVL",
        "moonshotai/Kimi-VL-A3B-Thinking",
        "",
        ModelClass.KimiVL,
        MaxImagesPerApiCallConfig(max_num_image=16, total_demo_video_frames=2),
    )
    KIMI_VL_A3B_INSTRUCT = (
        "KimiVL",
        "moonshotai/Kimi-VL-A3B-Instruct",
        "",
        ModelClass.KimiVL,
        MaxImagesPerApiCallConfig(max_num_image=16, total_demo_video_frames=2),
    )
    GROUND_TRUTH_ORACLE_SANITY_CHECK = (
        "Ground-Truth-Oracle_Sanity-Check",
        "",
        "",
        ModelClass.GroundTruthOracle,
    )

    def get_model_instance(
        self, print_response, model_path=None, **kwargs
    ):
        return self.constructor.impl(
            api_key=os.getenv(self.api_key),
            model=self.model_name if model_path is None else model_path,
            print_response=print_response,
            system_message=SYSTEM_MESSAGES.get(self),
            **dataclasses.asdict(self.max_images_per_api_call),
            **kwargs,
        )

    @staticmethod
    def from_string(s):
        try:
            return ModelType[s.upper()]
        except KeyError:
            raise ValueError(f"Invalid model type: {s}")


# Add potential system messages here
# We don't use it in our evaluation, while only relying on the task description
SYSTEM_MESSAGES = {}

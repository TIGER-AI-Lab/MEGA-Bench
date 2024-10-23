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
    OpenAI = ("models.OpenAI", "OpenAI")
    Claude = ("models.Claude", "Claude")
    Gemini = ("models.Gemini", "Gemini")
    Qwen2VL = ("models.Qwen2VL", "Qwen2VL")
    InternVL = ("models.InternVL", "InternVL")
    LlavaOV = ("models.LlavaOV", "LlavaOV")
    Pixtral = ("models.Pixtral", "Pixtral")
    Phi3v = ("models.Phi3v", "Phi3v")
    GroundTruthOracle = ("models.GroundTruthOracle", "GroundTruthOracle")


class ModelType(Enum):

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
    )
    GEMINI_FLASH_002 = (
        "gemini_flash",
        "gemini-1.5-flash-002",
        "GEMINI_API_KEY",
        ModelClass.Gemini,
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
    )
    QWEN2_VL_72B = (
        "Qwen2_VL_72B",
        "Qwen/Qwen2-VL-72B-Instruct",
        "",
        ModelClass.Qwen2VL,
    )
    QWEN2_VL_7B = ("Qwen2_VL_7B", "Qwen/Qwen2-VL-7B-Instruct", "", ModelClass.Qwen2VL)
    QWEN2_VL_2B = ("Qwen2_VL_2B", "Qwen/Qwen2-VL-2B-Instruct", "", ModelClass.Qwen2VL)
    INTERNVL2_LLAMA3_76B = (
        "InternVL2-Llama3-76B",
        "OpenGVLab/InternVL2-Llama3-76B",
        "",
        ModelClass.InternVL,
    )
    INTERNVL2_8B = ("InternVL2-8B", "OpenGVLab/InternVL2-8B", "", ModelClass.InternVL)
    LLAVA_ONEVISION_72B = (
        "Llava_OneVision_72B",
        "lmms-lab/llava-onevision-qwen2-72b-ov-chat",
        "",
        ModelClass.LlavaOV,
    )
    LLAVA_ONEVISION_7B = (
        "Llava_OneVision_7B",
        "lmms-lab/llava-onevision-qwen2-7b-ov",
        "",
        ModelClass.LlavaOV,
    )
    PIXTRAL_12B = (
        "Pixtral-12B",
        "mistralai/Pixtral-12B-2409",
        "",
        ModelClass.Pixtral,
    )
    PHI_3_5_VISION = (
        "Phi_3_5_vision",
        "microsoft/Phi-3.5-vision-instruct",
        "",
        ModelClass.Phi3v,
    )
    GROUND_TRUTH_ORACLE_SANITY_CHECK = (
        "Ground-Truth-Oracle_Sanity-Check",
        "",
        "",
        ModelClass.GroundTruthOracle,
    )

    def __init__(self, key: str, model_name: str, api_key: str, constructor: type):
        self.key = key
        self.model_name = model_name
        self.api_key = api_key
        self.constructor = constructor

    def get_model_instance(
        self, print_response, use_cot=False, model_path=None, **kwargs
    ):
        return self.constructor.impl(
            api_key=os.getenv(self.api_key),
            model=self.model_name if model_path is None else model_path,
            print_response=print_response,
            use_cot=use_cot,
            system_message=SYSTEM_MESSAGES.get(self),
            **MAX_IMAGES_PER_API_CALL[self],
            **kwargs,
        )

    @staticmethod
    def from_string(s):
        try:
            return ModelType[s.upper()]
        except KeyError:
            raise ValueError(f"Invalid model type: {s}")


MAX_IMAGES_PER_API_CALL = {
    ModelType.GPT_4O_0513: {
        "max_num_image": 64,
        "total_demo_video_frames": 8,
    },
    ModelType.GPT_4O_0806: {
        "max_num_image": 64,
        "total_demo_video_frames": 8,
    },
    ModelType.GPT_4O_MINI: {
        "max_num_image": 64,
        "total_demo_video_frames": 8,
    },
    ModelType.CLAUDE_3_HAIKU: {
        "max_num_image": 64,
        "total_demo_video_frames": 8,
    },
    ModelType.CLAUDE_3_5_SONNET: {
        "max_num_image": 64,
        "total_demo_video_frames": 8,
    },
    ModelType.CLAUDE_3_OPUS: {
        "max_num_image": 64,
        "total_demo_video_frames": 8,
    },
    ModelType.GEMINI_PRO: {
        "max_num_image": 128,
        "total_demo_video_frames": 16,
    },
    ModelType.GEMINI_PRO_002: {
        "max_num_image": 128,
        "total_demo_video_frames": 16,
    },
    ModelType.GEMINI_FLASH: {
        "max_num_image": 128,
        "total_demo_video_frames": 16,
    },
    ModelType.GEMINI_FLASH_002: {
        "max_num_image": 128,
        "total_demo_video_frames": 16,
    },
    ModelType.QWEN2_VL_7B: {
        "max_num_image": 18,
        "total_demo_video_frames": 2,
    },
    ModelType.QWEN2_VL_2B: {
        "max_num_image": 16,
        "total_demo_video_frames": 2,
    },
    ModelType.QWEN2_VL_72B: {
        "max_num_image": 24,
        "total_demo_video_frames": 2,
    },
    ModelType.INTERNVL2_LLAMA3_76B: {
        "max_num_image": 24,
        "total_demo_video_frames": 4,
    },
    ModelType.INTERNVL2_8B: {
        "max_num_image": 18,
        "total_demo_video_frames": 2,
    },
    ModelType.LLAVA_ONEVISION_72B: {
        "max_num_image": 28,
        "total_demo_video_frames": 4,
    },
    ModelType.LLAVA_ONEVISION_7B: {
        "max_num_image": 20,
        "total_demo_video_frames": 4,
    },
    ModelType.PIXTRAL_12B: {
        "max_num_image": 48,
        "total_demo_video_frames": 6,
    },
    ModelType.PHI_3_5_VISION: {
        "max_num_image": 16,
        "total_demo_video_frames": 2,
    },
    ModelType.GROUND_TRUTH_ORACLE_SANITY_CHECK: {
        "max_num_image": 64,
        "total_demo_video_frames": 8,
    },
}


# Add potential system messages here
# We don't use it in our evaluation, while only relying on the task description
SYSTEM_MESSAGES = {}


from . import throttling


class ImportThrottlingPolicyMixin:
    throttle_classes = (throttling.ImportModeRateThrottle,)

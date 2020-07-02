from taiga.base import throttling


class LoginFailRateThrottle(throttling.GlobalThrottlingMixin, throttling.ThrottleByActionMixin, throttling.SimpleRateThrottle):
    scope = "login-fail"
    throttled_actions = ["create"]

    def throttle_success(self, request, view):
        return True

    def finalize(self, request, response, view):
        if response.status_code == 400:
            self.history.insert(0, self.now)
            self.cache.set(self.key, self.history, self.duration)


class RegisterSuccessRateThrottle(throttling.GlobalThrottlingMixin, throttling.ThrottleByActionMixin, throttling.SimpleRateThrottle):
    scope = "register-success"
    throttled_actions = ["register"]

    def throttle_success(self, request, view):
        return True

    def finalize(self, request, response, view):
        if response.status_code == 201:
            self.history.insert(0, self.now)
            self.cache.set(self.key, self.history, self.duration)


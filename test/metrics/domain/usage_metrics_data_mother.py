class UsageMetricsDataMother:
    @staticmethod
    def any() -> dict[str, str]:
        return {
            "ipy_version": "1.2.3",
            "operating_system": "linux",
            "python_version": "3.12",
            "command": "init",
            "success": True,
            "template": "clean_architecture",
            "built_in_features": ["makefile"],
            "error_message": None,
        }

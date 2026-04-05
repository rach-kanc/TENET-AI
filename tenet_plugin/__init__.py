"""Framework-agnostic TENET AI security plugin."""

from .client import TenetSecurityPlugin, TenetPluginError

__all__ = ["TenetSecurityPlugin", "TenetPluginError"]

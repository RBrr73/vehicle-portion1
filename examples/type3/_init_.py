try:
    import pkg_resources
    pkg_resources.declare_namespace(__file__, __name__)
except ImportError:
    import pkgutil
    __path__ = pkgutil.extend_path(__path__, __name__)


    import pkg_resources
    import test_suite
    import name
    pkg_resources.declare_namespace(__name__)
master
except ImportError:
    import pkgutil
    __path__ = pkgutil.extend_path(__path__, __name__)

from telnet_server.models import Version


def check_update(current_ver: float):
    versions_in_base = Version.objects.filter(version__gt=current_ver).order_by("-version")
    if versions_in_base:
        return versions_in_base[0]
    return False

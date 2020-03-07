import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_script_file(host):
    file = host.file("/usr/bin/ipv6nat")
    assert file.exists
    assert file.user == "root"
    assert file.group == "root"
    assert file.mode == 0o774


def test_running_and_enabled(host):
    svc = host.service("ipv6nat")
    assert svc.is_running
    assert svc.is_enabled

import paramiko

username = 'root'
password = 'test0000'
host = '10.54.30.76'
cmd="ifconfig"


def ssh_run_remote_command(cmd):
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=host,
                           username=username,
                           password=password)
        stdin, stdout, stderr = ssh_client.exec_command(cmd)

        out = stdout.read().decode().strip()
        error = stderr.read().decode().strip()

        ssh_client.close()

        return out
print(ssh_run_remote_command(cmd))


# ====================================================


import io
import os
import re
import select
import socket
import time

import six
import paramiko
import pytest

from scp import SCPClient
from chainmap import ChainMap
from oslo_utils import encodeutils
from sshtunnel import SSHTunnelForwarder


# from logger import get_logger
import logging

log = logging.getLogger(__name__)

NON_NONE_DEFAULT = object()


def ssh_tunnel(host_ip, port, ssh_user, ssh_key_path,
               lbind_address, rbind_address):
    """Create SSH Tunnel."""
    server = SSHTunnelForwarder(
        (host_ip, port),
        ssh_username=ssh_user,
        ssh_pkey=ssh_key_path,
        local_bind_address=lbind_address,
        remote_bind_address=rbind_address,
        set_keepalive=1,
    )

    return server


def ssh_exec(host, command, ssh_user=None, ssh_pass=None,
             ssh_key_path=None, timeout=None):
    """Execute command on the SSH host and return it's output."""
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    stdout = ""
    try:
        client.connect(host, username=ssh_user,
                       password=ssh_pass, key_filename=ssh_key_path)
        _, stdout_lines, _ = client.exec_command(command, timeout=timeout)
        stdout = '\n'.join(stdout_lines)
    except Exception as e:
        err = "Error while connecting to {} via SSH: {}".format(host, e)
        log.error(err)
        pytest.fail(err)
    finally:
        client.close()
    return stdout


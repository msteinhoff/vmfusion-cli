# vmfusion-cli - command line interface for VMware Fusion

Minimal GUI replacement for the VMware Fusion GUI, e.g. for headless servers.

# Installation

    $ pip install vmfusion-cli

Tested with python 2.7.8.

# Overview

## Client configuration

A client configuration can be created at `~/.vmfusion.yml` to configure the path
to the `vmrun` command. If not configured, the path defaults to
`/Applications/VMware\ Fusion.app/Contents/Library/vmrun`.

## Library

The CLI uses a virtual machine library file to define available virtual machines
and their filesystem location.

Also, VM groups can be created to control multiple VMs at once. The VMs within a
group are ordered and that order is respected when e.g. starting or stopping a
group.

If no library path is given, library path defaults to `~/.vmfusion-library.yml`.

Sample configuration:

    ---
    machines:
        dev-vm1: /Users/Shared/Virtual Machines/dev-vm1/redhat.vmx
        dev-vm1: /Users/Shared/Virtual Machines/dev-vm1/redhat.vmx
        test-vm1: /Users/Shared/Virtual Machines/test-vm1/redhat.vmx
        test-vm2: /Users/Shared/Virtual Machines/test-vm2/redhat.vmx
    groups:
        devenv:
        - dev-vm1
        - dev-vm2
        testenv:
        - test-vm1
        - test-vm2

## Usage

The client can be used to list, start and stop VMs defined in the library.

### Status

To check the status of all registered VMs, use the `status` sub-command:

    $ vmfusion-cli [-l library.yml] status
    dev-vm1: running
    dev-vm1: running
    test-vm1: stopped
    test-vm2: stopped

### Start, Stop, Restart

VMs and VM groups can be controlled via standard sub-commands:

    $ vmfusion-cli [-l library.yml] [start|stop|restart] [vm-name|group-name]

# Contribution

Fork, code, pull request :)

# License

See LICENSE.txt

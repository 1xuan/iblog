# systemd and systemctl and service

- *short answer*: 

    - `systemd`(system deamon): systemd is a system and service manager for Linux operating systems.  When run as first process on boot (as PID 1), it acts as init system that brings up and maintains userspace services.

    - `systemctl`: systemctl may be used to introspect and control the state of the "systemd" system and service manager. It is a collection of system management libraries, utilities and daemons.

    - `service`: The service command is a wrapper script that allows system administrators to start, stop, and check the status of services without worrying too much about the actual init system being used.

## location

The package-provided service files are all usually located in `/lib/systemd/sytem. And show directories where services located:

~~~bash
$ man systemd.unit
~~~

## usage

- check service status

~~~bash
systemctl status servicename.service  # suffix is optional

# systemctl show servicename.service
~~~

- starting or stopping a service

~~~bash
systemctl start servicename  # systemctl stop servicename
~~~

~~~bash
service servicename start
~~~

**Reference**

[Difference between systemctl and service commands](https://askubuntu.com/questions/903354/difference-between-systemctl-and-service-commands/903405#903405)

[What is Systemctl? An In-Depth Overview](https://www.liquidweb.com/kb/what-is-systemctl-an-in-depth-overview/)

[How To Configure a Linux Service to Start Automatically After a Crash or Reboot – Part 1: Practical Examples](https://www.digitalocean.com/community/tutorials/how-to-configure-a-linux-service-to-start-automatically-after-a-crash-or-reboot-part-1-practical-examples)


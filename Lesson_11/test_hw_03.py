import pytest

from hw_03 import email_validator


def test_general():
  assert email_validator(r'username@hostname') is True
  assert email_validator(r'usernamehostname') is False


def test_username():
  assert email_validator(r'UserName@hostname') is True
  assert email_validator(r'User1name2@hostname') is True
  assert email_validator(r'0user1name2@hostname') is True
  assert email_validator(r'userName!@hostname') is True
  assert email_validator(r'user#name@hostname') is True
  assert email_validator(r'$user%name&@hostname') is True
  assert email_validator(r'‘*+—/=?^_`{|}~@hostname') is True
  assert email_validator(r'@hostname') is False
  assert email_validator(r'user:name@hostname') is False
  assert email_validator(r'user,name@hostname') is False
  assert email_validator(r'user;name@hostname') is False
  assert email_validator(r'user@name@hostname') is False
  assert email_validator(r'user\name@hostname') is False
  assert email_validator(r'user<name@hostname') is False
  assert email_validator(r'user>name@hostname') is False
  assert email_validator(r'user.name@hostname') is True
  assert email_validator(r'user..name@hostname') is False
  assert email_validator(r'user.na.me@hostname') is False
  assert email_validator(r'.username@hostname') is False
  assert email_validator(r'username.@hostname') is False


def test_hostname():
  assert email_validator(r'username@HostName') is True
  assert email_validator(r'username@1hostname') is True
  assert email_validator(r'username@host2name3') is True
  assert email_validator(r'username@host-name') is True
  assert email_validator(r'username@host.name') is True
  assert email_validator(r'username@ho.st.na.me') is True
  assert email_validator(r'username@ho-st.na--me') is True
  assert email_validator(r'username@HostNameHostNameHostNameHostNameHostNameHostNameHostNameHostNam') is True
  assert email_validator(r'username@HostNameHostNameHostNameHostNameHostNameHostNameHostNameHostName') is False
  assert email_validator(r'username@') is False
  assert email_validator(r'username@host!name') is False
  assert email_validator(r'username@host#name') is False
  assert email_validator(r'username@host$name') is False
  assert email_validator(r'username@host%name') is False
  assert email_validator(r'username@host&name') is False
  assert email_validator(r'username@host‘name') is False
  assert email_validator(r'username@host*name') is False
  assert email_validator(r'username@host+name') is False
  assert email_validator(r'username@host\name') is False
  assert email_validator(r'username@host|name') is False
  assert email_validator(r'username@host/name') is False
  assert email_validator(r'username@host=name') is False
  assert email_validator(r'username@host?name') is False
  assert email_validator(r'username@host^name') is False
  assert email_validator(r'username@host_name') is False
  assert email_validator(r'username@host`name') is False
  assert email_validator(r'username@host{name') is False
  assert email_validator(r'username@host}name') is False
  assert email_validator(r'username@host~name') is False
  assert email_validator(r'username@host:name') is False
  assert email_validator(r'username@host;name') is False
  assert email_validator(r'username@host<name') is False
  assert email_validator(r'username@host>name') is False
  assert email_validator(r'username@host,name') is False
  assert email_validator(r'username@host@name') is False
  assert email_validator(r'username@-host.name') is False
  assert email_validator(r'username@host-.name') is False
  assert email_validator(r'username@host.-name') is False
  assert email_validator(r'username@host.name-') is False

#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : sahara
Version  : 3.0.0
Release  : 4
URL      : http://tarballs.openstack.org/sahara/sahara-3.0.0.tar.gz
Source0  : http://tarballs.openstack.org/sahara/sahara-3.0.0.tar.gz
Summary  : Sahara project
Group    : Development/Tools
License  : Apache-2.0
Requires: sahara-bin
Requires: sahara-python
Requires: sahara-data
BuildRequires : Flask
BuildRequires : PyMySQL
BuildRequires : SQLAlchemy
BuildRequires : Sphinx
BuildRequires : Tempita
BuildRequires : WebOb
BuildRequires : Werkzeug
BuildRequires : alembic
BuildRequires : anyjson
BuildRequires : bashate
BuildRequires : cmd2
BuildRequires : coverage
BuildRequires : extras
BuildRequires : hacking
BuildRequires : itsdangerous
BuildRequires : jsonschema
BuildRequires : keystonemiddleware
BuildRequires : msgpack-python
BuildRequires : netaddr
BuildRequires : netifaces
BuildRequires : ordereddict
BuildRequires : oslo.db
BuildRequires : oslo.messaging
BuildRequires : oslo.middleware
BuildRequires : oslo.policy
BuildRequires : oslo.rootwrap
BuildRequires : oslo.service
BuildRequires : oslosphinx
BuildRequires : oslotest
BuildRequires : paramiko
BuildRequires : pbr
BuildRequires : pip
BuildRequires : psycopg2
BuildRequires : pylint
BuildRequires : pyparsing
BuildRequires : python-barbicanclient
BuildRequires : python-cinderclient
BuildRequires : python-dev
BuildRequires : python-editor
BuildRequires : python-heatclient
BuildRequires : python-manilaclient
BuildRequires : python-mimeparse
BuildRequires : python-mock
BuildRequires : python-neutronclient
BuildRequires : python-novaclient
BuildRequires : python-saharaclient
BuildRequires : python-swiftclient
BuildRequires : repoze.lru
BuildRequires : rfc3986
BuildRequires : setuptools
BuildRequires : sphinxcontrib-httpdomain
BuildRequires : sqlalchemy-migrate
BuildRequires : sqlparse
BuildRequires : stevedore
BuildRequires : tempest-lib
BuildRequires : testrepository
BuildRequires : traceback2
BuildRequires : unittest2
Patch1: 0001-Add-default-conf-file.patch
Patch2: 0002-Modify-rootwrap-location.patch

%description
OpenStack Data Processing ("Sahara") project
============================================

%package bin
Summary: bin components for the sahara package.
Group: Binaries
Requires: sahara-data

%description bin
bin components for the sahara package.


%package data
Summary: data components for the sahara package.
Group: Data

%description data
data components for the sahara package.


%package python
Summary: python components for the sahara package.
Group: Default
Requires: keystonemiddleware
Requires: stevedore

%description python
python components for the sahara package.


%prep
%setup -q -n sahara-3.0.0
%patch1 -p1
%patch2 -p1

%build
python2 setup.py build -b py2

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python3 setup.py test ||:
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/_sahara-subprocess
/usr/bin/sahara-all
/usr/bin/sahara-api
/usr/bin/sahara-db-manage
/usr/bin/sahara-engine
/usr/bin/sahara-rootwrap
/usr/bin/sahara-templates

%files data
%defattr(-,root,root,-)
/usr/share/sahara/README-sahara.conf.txt
/usr/share/sahara/compute.topology.sample
/usr/share/sahara/policy.json
/usr/share/sahara/rootwrap.conf
/usr/share/sahara/rootwrap.d/sahara.filters
/usr/share/sahara/sahara.conf.sample
/usr/share/sahara/sahara.conf.sample-basic
/usr/share/sahara/swift.topology.sample

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*

Summary:	Extra sounds for Asterisk
Name:		asterisk-sounds-extra
Version:	1.4.10
Release:	1
License:	CC-BY-SA
Group:		Applications/Sound
URL:		http://www.asterisk.org/
Source0:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-extra-sounds-en-alaw-%{version}.tar.gz
# Source0-md5:	7c5ad7b9c2655ccd98828243863f180d
Source1:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-extra-sounds-en-g722-%{version}.tar.gz
# Source1-md5:	1a2f12214dc03e9e1e2b0d44261e308e
Source2:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-extra-sounds-en-g729-%{version}.tar.gz
# Source2-md5:	74b71c02221280724e6116a7e5577501
Source3:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-extra-sounds-en-gsm-%{version}.tar.gz
# Source3-md5:	4c2af649a7c8df071c0da9629f6b00dc
Source4:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-extra-sounds-en-siren7-%{version}.tar.gz
# Source4-md5:	372f0a94f0dbca228340bf7358bdf043
Source5:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-extra-sounds-en-siren14-%{version}.tar.gz
# Source5-md5:	9be32e54b3ab15dfc0435f4c691948c0
Source6:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-extra-sounds-en-sln16-%{version}.tar.gz
# Source6-md5:	85adbb9798c85b8dbc445d2aa6030e92
Source7:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-extra-sounds-en-ulaw-%{version}.tar.gz
# Source7-md5:	69fab2dafe53e16a944e093f978fb02b
Source8:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-extra-sounds-en-wav-%{version}.tar.gz
# Source8-md5:	9a220b2d2f04f750719662d9ffc4034f
#Source10:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-extra-sounds-es-alaw-%{version}.tar.gz
## Source10-md5:	b0e8b6f39564a0d5f6d65a15994d26e2
#Source11:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-extra-sounds-es-g722-%{version}.tar.gz
## Source11-md5:	e0d1ddd6704e6f09c02b9ec2b0c4d340
#Source12:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-extra-sounds-es-g729-%{version}.tar.gz
## Source12-md5:	8c515c13ea40061509a93e2a601e2aeb
#Source13:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-extra-sounds-es-gsm-%{version}.tar.gz
## Source13-md5:	618fce9e53e3da2e7355a1b6d37df94d
#Source14:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-extra-sounds-es-siren7-%{version}.tar.gz
## Source14-md5:	4f2d65211bf6c607403348a45511d8d4
#Source15:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-extra-sounds-es-siren14-%{version}.tar.gz
## Source15-md5:	ffe3bc356ff2b1760c961d5a7d217396
#Source16:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-extra-sounds-es-sln16-%{version}.tar.gz
## Source16-md5:	337e5fe779a33a47cb4bd7403865d1d0
#Source17:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-extra-sounds-es-ulaw-%{version}.tar.gz
## Source17-md5:	bb81ed607e78dfbe6e9682287fb564a3
#Source18:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-extra-sounds-es-wav-%{version}.tar.gz
## Source18-md5:	5973a86090c58cf963c3a59c74eac0e1
Source20:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-extra-sounds-fr-alaw-%{version}.tar.gz
# Source20-md5:	a382b6a4b264570134551134431e76a7
Source21:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-extra-sounds-fr-g722-%{version}.tar.gz
# Source21-md5:	6f6b2cb44a0624d209d574438adc89f1
Source22:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-extra-sounds-fr-g729-%{version}.tar.gz
# Source22-md5:	9d68d59f251bbb0b3fdce21f6a324c77
Source23:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-extra-sounds-fr-gsm-%{version}.tar.gz
# Source23-md5:	f71dc7e574c640da80c21ed74323e8de
Source24:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-extra-sounds-fr-siren7-%{version}.tar.gz
# Source24-md5:	49d0f781cecf0ed9fc890b22fdf72a1c
Source25:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-extra-sounds-fr-siren14-%{version}.tar.gz
# Source25-md5:	38bad8bea6d915114d4000d3c1bda1db
Source26:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-extra-sounds-fr-sln16-%{version}.tar.gz
# Source26-md5:	c5948b2cba26191556a705812c2fed79
Source27:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-extra-sounds-fr-ulaw-%{version}.tar.gz
# Source27-md5:	8cf5b202fa43e75ecd9b248c8e523f96
Source28:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-extra-sounds-fr-wav-%{version}.tar.gz
# Source28-md5:	9872204d353bf516edbb028929b34d83
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		sounds_dir	%{_datadir}/asterisk/sounds

%description
Extra sound files for Asterisk.

%package en
Summary:	Extra English sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0

%description en
Extra English sound files for Asterisk.

%package en-alaw
Summary:	Extra English ALAW sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0
Requires:	asterisk-sounds-extra-en = %{version}-%{release}
Provides:	asterisk-sounds-extra = %{version}-%{release}

%description en-alaw
Extra English ALAW sound files for Asterisk.

%package en-g722
Summary:	Extra English G.722 sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0
Requires:	asterisk-sounds-extra-en = %{version}-%{release}
Provides:	asterisk-sounds-extra = %{version}-%{release}

%description en-g722
Extra English G.722 sound files for Asterisk.

%package en-g729
Summary:	Extra English G.729 sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0
Requires:	asterisk-sounds-extra-en = %{version}-%{release}
Provides:	asterisk-sounds-extra = %{version}-%{release}

%description en-g729
Extra English G.729 sound files for Asterisk.

%package en-gsm
Summary:	Extra English GSM sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0
Requires:	asterisk-sounds-extra-en = %{version}-%{release}
Provides:	asterisk-sounds-extra = %{version}-%{release}

%description en-gsm
Extra English GSM sound files for Asterisk.

%package en-siren7
Summary:	Extra English Siren7 sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0
Requires:	asterisk-sounds-extra-en = %{version}-%{release}
Provides:	asterisk-sounds-extra = %{version}-%{release}

%description en-siren7
Extra English Siren7 sound files for Asterisk.

%package en-siren14
Summary:	Extra English GSM sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0
Requires:	asterisk-sounds-extra-en = %{version}-%{release}
Provides:	asterisk-sounds-extra = %{version}-%{release}

%description en-siren14
Extra English Siren14 sound files for Asterisk.

%package en-sln16
Summary:	Extra English SLN16 sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0
Requires:	asterisk-sounds-extra-en = %{version}-%{release}
Provides:	asterisk-sounds-extra = %{version}-%{release}

%description en-sln16
Extra English SLN16 sound files for Asterisk.

%package en-ulaw
Summary:	Extra English ULAW sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0
Requires:	asterisk-sounds-extra-en = %{version}-%{release}
Provides:	asterisk-sounds-extra = %{version}-%{release}

%description en-ulaw
Extra English ULAW sound files for Asterisk.

%package en-wav
Summary:	Extra English WAV sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0
Requires:	asterisk-sounds-extra-en = %{version}-%{release}
Provides:	asterisk-sounds-extra = %{version}-%{release}

%description en-wav
Extra English WAV sound files for Asterisk.

%package es
Summary:	Extra Spanish sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0

%description es
Extra Spanish sound files for Asterisk.

%package es-alaw
Summary:	Extra Spanish ALAW sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0
Requires:	asterisk-sounds-extra-es = %{version}-%{release}
Provides:	asterisk-sounds-extra = %{version}-%{release}

%description es-alaw
Extra Spanish ALAW sound files for Asterisk.

%package es-g722
Summary:	Extra Spanish G.722 sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0
Requires:	asterisk-sounds-extra-es = %{version}-%{release}
Provides:	asterisk-sounds-extra = %{version}-%{release}

%description es-g722
Extra Spanish G.722 sound files for Asterisk.

%package es-g729
Summary:	Extra Spanish G.729 sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0
Requires:	asterisk-sounds-extra-es = %{version}-%{release}
Provides:	asterisk-sounds-extra = %{version}-%{release}

%description es-g729
Extra Spanish G.729 sound files for Asterisk.

%package es-gsm
Summary:	Extra Spanish GSM sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0
Requires:	asterisk-sounds-extra-es = %{version}-%{release}
Provides:	asterisk-sounds-extra = %{version}-%{release}

%description es-gsm
Extra Spanish GSM sound files for Asterisk.

%package es-siren7
Summary:	Extra Spanish Siren7 sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0
Requires:	asterisk-sounds-extra-es = %{version}-%{release}
Provides:	asterisk-sounds-extra = %{version}-%{release}

%description es-siren7
Extra Spanish Siren7 sound files for Asterisk.

%package es-siren14
Summary:	Extra Spanish Siren14 sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0
Requires:	asterisk-sounds-extra-es = %{version}-%{release}
Provides:	asterisk-sounds-extra = %{version}-%{release}

%description es-siren14
Extra Spanish Siren14 sound files for Asterisk.

%package es-sln16
Summary:	Extra Spanish SLN16 sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0
Requires:	asterisk-sounds-extra-es = %{version}-%{release}
Provides:	asterisk-sounds-extra = %{version}-%{release}

%description es-sln16
Extra Spanish SLN16 sound files for Asterisk.

%package es-ulaw
Summary:	Extra Spanish ULAW sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0
Requires:	asterisk-sounds-extra-es = %{version}-%{release}
Provides:	asterisk-sounds-extra = %{version}-%{release}

%description es-ulaw
Extra Spanish ULAW sound files for Asterisk.

%package es-wav
Summary:	Extra Spanish WAV sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0
Requires:	asterisk-sounds-extra-es = %{version}-%{release}
Provides:	asterisk-sounds-extra = %{version}-%{release}

%description es-wav
Extra Spanish WAV sound files for Asterisk.

%package fr
Summary:	Extra English sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0

%description fr
Extra French sound files for Asterisk.

%package fr-alaw
Summary:	Extra French ALAW sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0
Requires:	asterisk-sounds-extra-fr = %{version}-%{release}
Provides:	asterisk-sounds-extra = %{version}-%{release}

%description fr-alaw
Extra French ALAW sound files for Asterisk.

%package fr-g722
Summary:	Extra French G.722 sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0
Requires:	asterisk-sounds-extra-fr = %{version}-%{release}
Provides:	asterisk-sounds-extra = %{version}-%{release}

%description fr-g722
Extra French G.722 sound files for Asterisk.

%package fr-g729
Summary:	Extra French G.729 sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0
Requires:	asterisk-sounds-extra-fr = %{version}-%{release}
Provides:	asterisk-sounds-extra = %{version}-%{release}

%description fr-g729
Extra French G.729 sound files for Asterisk.

%package fr-gsm
Summary:	Extra French GSM sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0
Requires:	asterisk-sounds-extra-fr = %{version}-%{release}
Provides:	asterisk-sounds-extra = %{version}-%{release}

%description fr-gsm
Extra French GSM sound files for Asterisk.

%package fr-siren7
Summary:	Extra French Siren7 sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0
Requires:	asterisk-sounds-extra-fr = %{version}-%{release}
Provides:	asterisk-sounds-extra = %{version}-%{release}

%description fr-siren7
Extra French Siren7 sound files for Asterisk.

%package fr-siren14
Summary:	Extra French Siren14 sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0
Requires:	asterisk-sounds-extra-fr = %{version}-%{release}
Provides:	asterisk-sounds-extra = %{version}-%{release}

%description fr-siren14
Extra French Siren14 sound files for Asterisk.

%package fr-sln16
Summary:	Extra French SLN16 sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0
Requires:	asterisk-sounds-extra-fr = %{version}-%{release}
Provides:	asterisk-sounds-extra = %{version}-%{release}

%description fr-sln16
Extra French SLN16 sound files for Asterisk.

%package fr-ulaw
Summary:	Extra French ULAW sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0
Requires:	asterisk-sounds-extra-fr = %{version}-%{release}
Provides:	asterisk-sounds-extra = %{version}-%{release}

%description fr-ulaw
Extra French ULAW sound files for Asterisk.

%package fr-wav
Summary:	Extra French WAV sound files for Asterisk
Group:		Applications/Sound
Requires:	asterisk >= 1.4.0
Requires:	asterisk-sounds-extra-fr = %{version}-%{release}
Provides:	asterisk-sounds-extra = %{version}-%{release}

%description fr-wav
Extra French WAV sound files for Asterisk.

%prep
%setup -q -c -T

if [ -f /proc/$PPID/environ ]; then
	# import env from parent process
	unset LC_ALL
	export $(tr '\0' '\n' < /proc/$PPID/environ | grep -E '^(LC_|LANG)')
	if locale | grep -Eqi 'utf-?8'; then
		echo >&2 "You should re-run rpmbuild with LANG=C LC_ALL=C, see https://bugs.launchpad.net/pld-linux/+bug/501593"
		exit 1
	fi
fi

for file in %{S:0} %{S:1} %{S:2} %{S:3} %{S:4} %{S:5} %{S:6} %{S:7} %{S:8}; do
	tar --list --file $file | grep -E '.(alaw|g722|g729|gsm|siren7|siren14|sln16|ulaw|wav)$' | sed -e 's!^!%{sounds_dir}/!' > `basename $file .tar.gz`.list
	tar --extract --directory . --file $file
done

#mkdir es
#for file in %{S:10} %{S:11} %{S:12} %{S:13} %{S:14} %{S:15} %{S:16} %{S:17} %{S:18}; do
#	tar --list --file $file | grep -E '.(alaw|g722|g729|gsm|siren7|siren14|sln16|ulaw|wav)$' | sed -e 's!^!%{sounds_dir}/es/!' > `basename $file .tar.gz`.list
#	tar --extract --directory ./es/ --file $file
#done

mkdir fr
for file in %{S:20} %{S:21} %{S:22} %{S:23} %{S:24} %{S:25} %{S:26} %{S:27} %{S:28}; do
	tar --list --file $file | grep -E '.(alaw|g722|g729|gsm|siren7|siren14|sln16|ulaw|wav)$' | sed -e 's!^!%{sounds_dir}/fr/!' > `basename $file .tar.gz`.list
	tar --extract --directory ./fr/  --file $file
done

iconv -f iso-8859-1 -t utf-8 < fr/extra-sounds-fr.txt > fr/extra-sounds-fr.txt.tmp
touch --reference fr/extra-sounds-fr.txt fr/extra-sounds-fr.txt.tmp
mv fr/extra-sounds-fr.txt.tmp fr/extra-sounds-fr.txt

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{sounds_dir}/{,es,fr}

for file in $(cat *.list | sed -e 's!^%{sounds_dir}/!!'); do
	install -d $RPM_BUILD_ROOT%{sounds_dir}/$(dirname $file)
	cp -p $file $RPM_BUILD_ROOT%{sounds_dir}/$file
done

%clean
rm -rf $RPM_BUILD_ROOT

%files en
%defattr(644,root,root,755)
%doc extra-sounds-en.txt
%doc CHANGES-asterisk-extra-en-%{version}
%dir %{sounds_dir}/ha/
%dir %{sounds_dir}/wx/

%files en-alaw -f asterisk-extra-sounds-en-alaw-%{version}.list
%defattr(644,root,root,755)
%doc asterisk-extra-sounds-en-alaw-%{version}.list

%files en-g722 -f asterisk-extra-sounds-en-g722-%{version}.list
%defattr(644,root,root,755)
%doc asterisk-extra-sounds-en-g722-%{version}.list

%files en-g729 -f asterisk-extra-sounds-en-g729-%{version}.list
%defattr(644,root,root,755)
%doc asterisk-extra-sounds-en-g729-%{version}.list

%files en-gsm -f asterisk-extra-sounds-en-gsm-%{version}.list
%defattr(644,root,root,755)
%doc asterisk-extra-sounds-en-gsm-%{version}.list

%files en-siren7 -f asterisk-extra-sounds-en-siren7-%{version}.list
%defattr(644,root,root,755)
%doc asterisk-extra-sounds-en-siren7-%{version}.list

%files en-siren14 -f asterisk-extra-sounds-en-siren14-%{version}.list
%defattr(644,root,root,755)
%doc asterisk-extra-sounds-en-gsm-%{version}.list

%files en-sln16 -f asterisk-extra-sounds-en-sln16-%{version}.list
%defattr(644,root,root,755)
%doc asterisk-extra-sounds-en-sln16-%{version}.list

%files en-ulaw -f asterisk-extra-sounds-en-ulaw-%{version}.list
%defattr(644,root,root,755)
%doc asterisk-extra-sounds-en-ulaw-%{version}.list

%files en-wav -f asterisk-extra-sounds-en-wav-%{version}.list
%defattr(644,root,root,755)
%doc asterisk-extra-sounds-en-wav-%{version}.list

%if 0
%files es
%defattr(644,root,root,755)
%doc es/extra-sounds-es.txt
%doc es/CHANGES-asterisk-extra-es-%{version}
%doc es/CREDITS-asterisk-extra-es-%{version}
%doc es/LICENSE-asterisk-extra-es-%{version}
%dir %{sounds_dir}/es/ha/
%dir %{sounds_dir}/es/wx/

%files es-alaw -f asterisk-extra-sounds-es-alaw-%{version}.list
%defattr(644,root,root,755)
%doc asterisk-extra-sounds-es-alaw-%{version}.list

%files es-g722 -f asterisk-extra-sounds-es-g722-%{version}.list
%defattr(644,root,root,755)
%doc asterisk-extra-sounds-es-g722-%{version}.list

%files es-g729 -f asterisk-extra-sounds-es-g729-%{version}.list
%defattr(644,root,root,755)
%doc asterisk-extra-sounds-es-g729-%{version}.list

%files es-gsm -f asterisk-extra-sounds-es-gsm-%{version}.list
%defattr(644,root,root,755)
%doc asterisk-extra-sounds-es-gsm-%{version}.list

%files es-siren7 -f asterisk-extra-sounds-es-siren7-%{version}.list
%defattr(644,root,root,755)
%doc asterisk-extra-sounds-es-siren7-%{version}.list

%files es-siren14 -f asterisk-extra-sounds-es-siren14-%{version}.list
%defattr(644,root,root,755)
%doc asterisk-extra-sounds-es-siren14-%{version}.list

%files es-sln16 -f asterisk-extra-sounds-es-sln16-%{version}.list
%defattr(644,root,root,755)
%doc asterisk-extra-sounds-es-sln16-%{version}.list

%files es-ulaw -f asterisk-extra-sounds-es-ulaw-%{version}.list
%defattr(644,root,root,755)
%doc asterisk-extra-sounds-es-ulaw-%{version}.list

%files es-wav -f asterisk-extra-sounds-es-wav-%{version}.list
%defattr(644,root,root,755)
%doc asterisk-extra-sounds-es-wav-%{version}.list
%endif

%files fr
%defattr(644,root,root,755)
%doc fr/extra-sounds-fr.txt
%doc fr/CHANGES-asterisk-extra-fr-%{version}
%doc fr/CHANGES-asterisk-extra-fr-1.4.txt
%doc fr/CREDITS-core-extra-fr.txt
%doc fr/MISSING.txt
%dir %{sounds_dir}/fr/ha/
%dir %{sounds_dir}/fr/wx/

%files fr-alaw -f asterisk-extra-sounds-fr-alaw-%{version}.list
%defattr(644,root,root,755)
%doc asterisk-extra-sounds-fr-alaw-%{version}.list

%files fr-g722 -f asterisk-extra-sounds-fr-g722-%{version}.list
%defattr(644,root,root,755)
%doc asterisk-extra-sounds-fr-g722-%{version}.list

%files fr-g729 -f asterisk-extra-sounds-fr-g729-%{version}.list
%defattr(644,root,root,755)
%doc asterisk-extra-sounds-fr-g729-%{version}.list

%files fr-gsm -f asterisk-extra-sounds-fr-gsm-%{version}.list
%defattr(644,root,root,755)
%doc asterisk-extra-sounds-fr-gsm-%{version}.list

%files fr-siren7 -f asterisk-extra-sounds-fr-siren7-%{version}.list
%defattr(644,root,root,755)
%doc asterisk-extra-sounds-fr-siren7-%{version}.list

%files fr-siren14 -f asterisk-extra-sounds-fr-siren14-%{version}.list
%defattr(644,root,root,755)
%doc asterisk-extra-sounds-fr-siren14-%{version}.list

%files fr-sln16 -f asterisk-extra-sounds-fr-sln16-%{version}.list
%defattr(644,root,root,755)
%doc asterisk-extra-sounds-fr-sln16-%{version}.list

%files fr-ulaw -f asterisk-extra-sounds-fr-ulaw-%{version}.list
%defattr(644,root,root,755)
%doc asterisk-extra-sounds-fr-ulaw-%{version}.list

%files fr-wav -f asterisk-extra-sounds-fr-wav-%{version}.list
%defattr(644,root,root,755)
%doc asterisk-extra-sounds-fr-wav-%{version}.list

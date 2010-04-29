Summary:	Extra sounds for Asterisk
Name:		asterisk-sounds-extra
Version:	1.4.11
Release:	1
License:	CC-BY-SA
Group:		Applications/Sound
URL:		http://www.asterisk.org/
Source0:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-extra-sounds-en-alaw-%{version}.tar.gz
# Source0-md5:	3a0bfe79e9e83d12a4b519dab1dc4c48
Source1:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-extra-sounds-en-g722-%{version}.tar.gz
# Source1-md5:	be2bfa1ab8e52ed334798d11549653b1
Source2:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-extra-sounds-en-g729-%{version}.tar.gz
# Source2-md5:	ae5e738ab6b2b15834a907cdd982cb77
Source3:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-extra-sounds-en-gsm-%{version}.tar.gz
# Source3-md5:	5479cb4cb81d678304d96f35e4933a11
Source4:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-extra-sounds-en-siren7-%{version}.tar.gz
# Source4-md5:	38326a003d905fea32f4cad3b075ee0d
Source5:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-extra-sounds-en-siren14-%{version}.tar.gz
# Source5-md5:	cf518c3b4e8293680377a312d365e095
Source6:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-extra-sounds-en-sln16-%{version}.tar.gz
# Source6-md5:	1ed34b754c9729f45a290441d458eede
Source7:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-extra-sounds-en-ulaw-%{version}.tar.gz
# Source7-md5:	556a9b77235194644d6a7f7068d3ddaa
Source8:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-extra-sounds-en-wav-%{version}.tar.gz
# Source8-md5:	1dff0265f8051d4ee44d6772bd93d528
Source20:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-extra-sounds-fr-alaw-%{version}.tar.gz
# Source20-md5:	6423eeab5fa32797f318147095bdfbb1
Source21:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-extra-sounds-fr-g722-%{version}.tar.gz
# Source21-md5:	3253a6c1ff07301f63b069aaa911c132
Source22:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-extra-sounds-fr-g729-%{version}.tar.gz
# Source22-md5:	a06e5e08335df9d2ec2617095998b638
Source23:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-extra-sounds-fr-gsm-%{version}.tar.gz
# Source23-md5:	bd72c1f57f9e1ab64ee109612aa2ae7b
Source24:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-extra-sounds-fr-siren7-%{version}.tar.gz
# Source24-md5:	64b4115558eeb1d0d501f9da96852eff
Source25:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-extra-sounds-fr-siren14-%{version}.tar.gz
# Source25-md5:	4e1daf6f7f1e74447719ef070cdcab39
Source26:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-extra-sounds-fr-sln16-%{version}.tar.gz
# Source26-md5:	76e559d433fba3b0017d4a5635319b86
Source27:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-extra-sounds-fr-ulaw-%{version}.tar.gz
# Source27-md5:	7b2050a9e2363104b12f7394ca2db8d1
Source28:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-extra-sounds-fr-wav-%{version}.tar.gz
# Source28-md5:	e7836238d8d74dcecf72f384731217f9
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
%setup -qcT

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
install -d $RPM_BUILD_ROOT%{sounds_dir}/{,fr}

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
%dir %{sounds_dir}/ha
%dir %{sounds_dir}/wx

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

%files fr
%defattr(644,root,root,755)
%doc fr/extra-sounds-fr.txt
%doc fr/CHANGES-asterisk-extra-fr-%{version}
%doc fr/CHANGES-asterisk-extra-fr-1.4.txt
%doc fr/CREDITS-core-extra-fr.txt
%doc fr/MISSING.txt
%dir %{sounds_dir}/fr/ha
%dir %{sounds_dir}/fr/wx

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

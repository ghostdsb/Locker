import data as d
import encryption,decryption,mEncryption
import pprint

def PasswordAdding():
	user = input('user: ')
	mpass = input('Master Password: ')
	site = input('site: ').lower()
	loginId = input('site login id: ')
	password = input('site password: ')

	eUser = encryption.encryption(user,mpass)
	eSite = encryption.encryption(site,mpass)
	eLoginId = encryption.encryption(loginId,mpass)
	ePassword = encryption.encryption(password,mpass)
		

	if eUser not in d.data:
		d.data[eUser] = [mEncryption.encryption(mpass)]
		d.data[eUser] += [(eSite,eLoginId,ePassword)]
		
	elif eUser in d.data:
		if mEncryption.encryption(mpass) != d.data[eUser][0]:
			print('User with same name is present under different Master Password')
			read = input('Try adding adding again or continue?\n>')
			if 'again' in read or 'retry' in read:
				PasswordAdding()
			else:
				d.data[eUser] += [(eSite,eLoginId,ePassword)]
		else:
			d.data[eUser] += [(eSite,eLoginId,ePassword)]

		
	with open(r'F:\devs\py\locker\data.py','w') as w:
		w.write('data = ')
		w.write(pprint.pformat(d.data))



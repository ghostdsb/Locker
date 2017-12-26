import data as d
import encryption,decryption,mEncryption

def PasswordRetrieve():
	pfound = False
	user = input('user: ')
	mpass = input('master password: ')
	eUser = encryption.encryption(user,mpass)

	if eUser in d.data:
		if mEncryption.encryption(mpass) == d.data[eUser][0]:
			site = input('site: ')
			for q in d.data[eUser][1:]:
				if q[0] == encryption.encryption(site,mpass):
					print('login id: '+decryption.decryption(q[1],mpass))
					print('password: '+decryption.decryption(q[2],mpass))
					pfound = True
					break
			if not pfound:
				print('site not in database')
		else:
			print('Wrong master password')
	else:
		print('User not found')


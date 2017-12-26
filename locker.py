import password_adding_script as pas
import password_retrieval_script as prs

Y = ['yes','y']
N = ['no','n','stop']

work = input('Password adding or retrieving?\n>')

if 'add' in work or 'new' in work:
	pas.PasswordAdding()
	
else:
	prs.PasswordRetrieve()
	
	
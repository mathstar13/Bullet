import argparse
parser = argparse.ArgumentParser(description='The parser of the Bullet Programming Language.')
parser.add_argument('filename', metavar='F', help='The file to parse.')
args = parser.parse_args()
fn = args.filename
from ast import literal_eval as le
global var
var = {}
global function
function = {'RAISE': {'code': 'PYPARSE f\'error("$type" & "$text")\'\n', 'attrib': ['$type', '$text'], 'head': [], 'sl': 2}, 'FILE.READ': {'code': 'PYPARSE f\'setvar("$data" & open("$file" & "r").read())\'\nRETURN $data\n', 'attrib': ['$file'], 'head': [], 'sl': 6}, 'FILE.WRITE': {'code': 'PYPARSE f\'open("$file" & "w").write("$text")\'\nRETURN \'True\'\n', 'attrib': ['$file', '$text'], 'head': [], 'sl': 10}, 'QUIT': {'code': "PYPARSE f'quit($code)'\n", 'attrib': ["$code=''"], 'head': [], 'sl': 15}, 'VERSION': {'code': "RETURN '0.1'\n", 'attrib': [], 'head': [], 'sl': 18}, 'WAIT': {'code': "PYPARSE f'from time import sleep\\nsleep($AMM)'\n", 'attrib': ["$AMM='1'"], 'head': [], 'sl': 21}, 'GETFUNCTION': {'code': 'PYPARSE f\'setvar("$ret" & function["$fn"])\'\nRETURN $ret\n', 'attrib': ['$fn'], 'head': [], 'sl': 24}, 'APPEND_TO_FUNCTION': {'code': '$data = (STR.REPLACE(\'BTCODE13561346543643653463nl\',f\'\\n\'))\nPYPARSE f\'function["$name"] = .replace("BTCODE13561346543643653463nl","\\n"))\'\n', 'attrib': ['$name', '$fn'], 'head': [], 'sl': 28}, 'MATH.+': {'code': 'PYPARSE f\'setvar("$data" & str($n1+$n2))\'\nRETURN $data\n', 'attrib': ["$n1='0'", "$n2='0'"], 'head': [], 'sl': 33}, 'MATH.-': {'code': 'PYPARSE f\'setvar("$data" & str($n1-$n2))\'\nRETURN $data\n', 'attrib': ["$n1='0'", "$n2='0'"], 'head': [], 'sl': 37}, 'MATH.*': {'code': 'PYPARSE f\'setvar("$data" & str($n1*$n2))\'\nRETURN $data\n', 'attrib': ["$n1='0'", "$n2='0'"], 'head': [], 'sl': 41}, 'MATH./': {'code': 'PYPARSE f\'setvar("$data" & str($n1/$n2))\'\nRETURN $data\n', 'attrib': ["$n1='0'", "$n2='0'"], 'head': [], 'sl': 45}, 'STR.LEN': {'code': 'PYPARSE f\'setvar("$data" & len("$str"))\'\nRETURN $STR.$data\n', 'attrib': ['$str'], 'head': [], 'sl': 50}, 'STR.SPLIT': {'code': 'PYPARSE f\'setvar("$data" & "$str".split("$char"))\'\nRETURN $data\n', 'attrib': ['$str', "$char=' '"], 'head': [], 'sl': 54}, 'STR.REPLACE': {'code': 'IF $count != \'*\'{\nPYPARSE f"setvar(\'$data\' & \'$str\'.replace(\'$text\' & \'$repv\' & $count))"\n}\nELSE{\nPYPARSE f"setvar(\'\'\'$data\'\'\' & \'\'\'$str\'\'\'.replace(\'\'\'$text\'\'\' & \'\'\'$repv\'\'\'))"\n}\nRETURN $data\n', 'attrib': ['$str', '$text', '$repv', "$count='*'"], 'head': [], 'sl': 58}, 'STR.STARTSWITH': {'code': "IF $var.startswith($text){\nRETURN 'True'\n}\nELSE{\nRETURN 'False'\n}\n", 'attrib': ['$var', '$text'], 'head': [], 'sl': 67}, 'STR.GROUP': {'code': 'PYPARSE f\'setvar("$data" & "$str"+"$value")\'\nRETURN $data\n', 'attrib': ['$str', '$value'], 'head': [], 'sl': 75}, 'JSON.PARSE': {'code': 'PYPARSE f"from ast import literal_eval as le\\nsetvar(\'\'\'$data\'\'\' & le(\'\'\'$jsonstr\'\'\'))"\nRETURN $data\n', 'attrib': ['$jsonstr'], 'head': [], 'sl': 80}, 'FUNCTION_VAR': {'code': 'PYPARSE f\'setvar("$d" & function["$fn"]["head"])\'\nIF not \'no_function_var\' in $d{\nPYPARSE f\'setvar("$data" & var["$fn"]["$name"])\'\nRETURN $data\n}\nELSE{\nRAISE \'FunctionVarError\' & f\'FunctionVar blocked by function header: "no_function_var" in function "$fn".\'\n}\n', 'attrib': ['$fn', '$name'], 'head': [], 'sl': 85}, 'GET_FUNCTION_HEADERS': {'code': 'PYPARSE f\'setvar("$data" & function["$fn"]["head"])\'\nRETURN $data\n', 'attrib': ['$fn'], 'head': [], 'sl': 95}, 'INPUT': {'code': 'IN $data = $text\nRETURN $data\n', 'attrib': ['$text'], 'head': [], 'sl': 99}}
global d
d = {'atc':'not','count':0,'nl':'','if':True,'fn':fn,'err':'none','else':False,'em':'none','funct':'not','ov':{},'close-count':0,'st':True,'prefix':'','sendto':'not','retd':'not','evalparen':False}
global eh
eh = {}
def getvar(vn):
	if d['funct'] == 'not':
		return var[vn]
	else:
		return var[d['funct']][vn]
def charforeach(char,var):
	cnt = 0
	for c in var:
		if c == char:
			cnt += 1
	return cnt
def setvar(vn,vt,df=True):
	if df:
		if vt == 'NULL':
			del var[vn]
		else:
			if vn.startswith('$'):
				if d['prefix'] != '':
					vn = '$'+d['prefix']+vn
				if d['funct'] == 'not':
					var[vn] = vt
				else:
					var[d['funct']][vn] = vt
			else:
				vn = '$' + vn
				if d['prefix'] != '':
					vn = '$'+d['prefix']+vn
				if d['funct'] == 'not':
					var[vn] = vt
				else:
					var[d['funct']][vn] = vt
	else:
		if vt == 'NULL':
			del var[vn]
		else:
			if vn.startswith('$'):
				var[d['prefix']+vn] = vt
			else:
				vn = '$' + vn
				var[d['prefix']+vn] = vt
def checkvn(vn):
	if vn.startswith('$'):
		return True
	else:
		error('VarError','Variables must start with "$".')
def stringify(code,dc=True):
	code = code.replace(r'\n','\n').replace(r'\t','\t')
	oc = code
	code = listify(code)
	#if dc:
		#del code[length(code) - 1]
	co = True
	try:
		code[0]
	except IndexError:
		error('DataError','No data supplied for argument.')
		quit()
	try:
		code[1]
	except IndexError:
		co = False	
	if code[0] == '[' or code[0] == '{':
		return le(oc.replace('&',','))
	elif code[0] == '(':
		oretd = d['retd']
		d['retd'] = 'hwekjghwireytqiowir34oitygiorqjweq05utwguiodhg239ythgiof;lut834hhyregw9et7y345gkw369yu5io3pw3rheyywreoyho34iyrhio34\\\\\\\\\\\\\\\\\\\\\\wrey4ykhio46joi9458ojorep;y'
		parse(unlistify(code).replace('(','',1)[::-1].replace(')','',1)[::-1].replace(r'\;','*($KATDELKH%$GJOAHRSEMI*!').replace(';','\n').replace('*($KATDELKH%$GJOAHRSEMI*!',';'),'not')
		retd = d['retd']
		d['retd'] = oretd
		if retd == 'hwekjghwireytqiowir34oitygiorqjweq05utwguiodhg239ythgiof;lut834hhyregw9et7y345gkw369yu5io3pw3rheyywreoyho34iyrhio34\\\\\\\\\\\\\\\\\\\\\\wrey4ykhio46joi9458ojorep;y':
			return 'NULL'
		else:
			return retd
	elif oc.startswith('funct: '):
		return function[oc.replace('funct: ','',1)]
	elif code[0] == '$':
		try:
				if d['funct'] == 'not':
					return var[unlistify(code)]
				else:
					return var[d['funct']][unlistify(code)]
		except KeyError:
				error('VarError',f'Could not find var {oc}.')
				quit()
	elif code[0] == "'":
		ps = ''
		for item in code:
			if item != "'":
				ps += item
		return ps
	elif code[0] == '"':
		ps = ''
		for item in code:
			if item != '"':
				ps += item
		return ps
	elif co:
		if code[0] == '"' or code[1] == '"':
			ps = ''
			for item in code:
				if item != '"':
					ps += item
			if ps.startswith('f'):
				ps = ps.replace('f','',1)
				if d['funct'] == 'not':
					for vn,vt in var.items():
						if vn.startswith('$'):
							ps = ps.replace(vn,vt)
				else:
					for vn,vt in var[d['funct']].items():
						if vn.startswith('$'):
							ps = ps.replace(vn,vt)
				ps = ps.replace(r'\dollar','$').replace(r'\n','\n')
			return ps
		elif code[0] == "'" or code[1] == "'":
			ps = ''
			for item in code:
				if item != "'":
					ps += item
			if ps.startswith('f'):
				ps = ps.replace('f','',1)
				if d['funct'] == 'not':
					for vn,vt in var.items():
						if vn.startswith('$'):
							ps = str(ps).replace(str(vn),str(vt))
				else:
					for vn,vt in var[d['funct']].items():
						if vn.startswith('$'):
							ps = str(ps).replace(str(vn),str(vt))
				ps = ps.replace(r'\dollar','$').replace(r'\n','\n')
				return ps
	else:
		try:
			int(oc)
			oc = int(oc)
		except ValueError:
				error('DataError',f'Invalid Data: "{oc}"')
				quit()
def listify(string):
	l = []
	for char in string:
		l.append(char)
	return l
def unlistify(li):
	s = ''
	for item in li:
		s += item
	return s
def length(li):
	l = 0
	for item in li:
		l += 1
	return l
def out(code):
	print(stringify(code))
def callfunction(code,rq=False):
	from ast import literal_eval as le
	if code.split()[0] in function.keys():
		ofn = d['funct']
		functname = d['prefix']+code.split()[0]
		var[functname] = {}
		code = code.replace(functname + ' ','')
		c = 0
		if d['funct'] == 'not':
			for vn,vt in var.items():
				if type(vt) == str:
					code = code.replace(vn,f"'{vt}'")
				else:
					code = code.replace(vn,str(vt))
		else:
			for vn,vt in var[d['funct']].items():
				if type(vt) == str:
					code = code.replace(vn,f"'{vt}'")
				else:
					code = code.replace(vn,str(vt))
		d['funct'] = functname
		if code != '':
			attrib = ''
		else:
			attrib = ':('
		if attrib != ':(':
			for item in function[functname]['attrib']:
				try:
					try:
						item.split('=')[1]
						n = item.split('=')[0]
						opt = True
					except IndexError:
						n = item
						opt = False
					var[functname][n] = stringify(code.split(' & ')[c])
				except IndexError:
					if opt:
						var[functname][n] = stringify(item.split('=')[1])
					else:
						error('AttributeError',f'Missing required attribute "{item}".')
				c += 1
		code = function[functname]['code']
		oc = d['count']
		d['count'] = function[functname]['sl']
		for line in code.splitlines():
			parse(line,d['atc'])
			d['count'] += 1
		d['count'] = oc
		d['funct'] = ofn
	else:
		if code.split()[0].startswith('}'):
			pass
		else:
			error('SyntaxError',f'No function named {code.split()[0]}.')
def vari(code):
	code = listify(code)
	vn = ''
	vt = ''
	for char in code:
		if char == ' ':
			break
		else:
			vn += char
	if checkvn(vn):
		for char in vn:
			code.remove(char)
		code.remove('=')
		code.remove(' ')
		code.remove(' ')
		vt = stringify(unlistify(code))
		setvar(vn,vt)
def arr(code):
	from ast import literal_eval as le
	vn = code.split()[0]
	if checkvn(vn):
		code = code.replace(vn,'',1).replace(' = ','',1)
		setvar(vn,le('[' + code + ']'))
def IN(code):
	oc = code
	code = code.split()
	vn = code[0]
	if checkvn(vn):
		oc = oc.replace(f'{vn} = ','')
		if d['funct'] == 'not':
			var[d['prefix']+vn] = input(stringify(oc))
		else:
			var[d['funct']][d['prefix']+vn] = input(stringify(oc))
def fn(code):
	from ast import literal_eval as le
	global d
	if code.split()[0].startswith('['):
		d['atc'] = d['prefix']+code.split()[1]
		if d['atc'][::-1].startswith('{'):
			d['atc'] = d['atc'][::-1].replace('{','',1)[::-1]
		if d['atc'] in function.keys():
			if 'const' in function[d['atc']]['head']:
				error('ConstError',f'Const function "{d["atc"]}" already exists.')
				d['atc'] = 'not'
				return True
		function[d['atc']] = {}
		function[d['atc']]['code'] = ''
		function[d['atc']]['attrib'] = []
		function[d['atc']]['head'] = le(code.split()[0])
		code = code.replace(code.split()[0]+' ','',1)
	else:
		d['atc'] = d['prefix']+code.split()[0]
		if d['atc'][::-1].startswith('{'):
			d['atc'] = d['atc'][::-1].replace('{','',1)[::-1]
		if d['atc'] in function.keys():
			if 'const' in function[d['atc']]['head']:
				error('ConstError',f'Const function "{d["atc"]}" already exists.')
				d['atc'] = 'not'
				return True
		function[d['atc']] = {}
		function[d['atc']]['code'] = ''
		function[d['atc']]['attrib'] = []
		function[d['atc']]['head'] = []
	d['close-count'] = 1
	d['ov'] = var
	try:
		code.split()[1]
		s = True
	except IndexError:
		s = False
	code = code.replace(code.split()[0]+' ','',1)
	if s:
		for item in code.replace(d['atc']+' ','',1).split(' & '):
			if not item.startswith('$') and d['prefix'] != '':
				item = '$'+item
			if checkvn(item):
				if item[::-1].startswith('{'):
					item = item[::-1].replace('{','',1)[::-1]
				function[d['atc']]['attrib'].append(item)
	function[d['atc']]['sl'] = d['count']
def parsepy(code):
	exec(stringify(code))
def IF(code):
	code = code[::-1].replace('{','',1)[::-1]
	code = code[::-1].replace(';','',1)[::-1]
	if d['funct'] == 'not':
		for vn,vt in var.items():
				code = code.replace(vn,f'"{var[vn]}"')
		d['close-count'] += 1
	else:
		for vn,vt in var[d["funct"]].items():
			code = code.replace(vn,f'"{var[d["funct"]][vn]}"')
		d['close-count'] += 1
	code = code.replace(r'\dollar','$')
	if not eval(code):
		d['if'] = False
		d['else'] = True
		d['st'] = False
	else:
		d['if'] = True
		d['else'] = False
		d['st'] = True
def EVAL(code):
	atc = 'not'
	if code.startswith('"'):
		code = code.replace('"','',1)[::-1].replace('"','',1)[::-1]
	else:
		code = code.replace("'",'',1)[::-1].replace("'",'',1)[::-1]
	for line in code.splitlines():
		parse(line,atc)
def imp_file(fn):
	from ast import literal_eval as le
	try: 
		open(fn)
	except FileNotFoundError:
		return False
	for o,t in le(open(fn).read())['function'].items():
		function[o] = t
	for vn,vt in le(open(fn).read())['var'].items():
		var[vn] = vt
	try:
		function['__main__']
		main = True
	except KeyError:
		main = False
	if main:
		for line in function['__main__']['code'].splitlines():
			parse(line,d['atc'])
		del function['__main__']
def get(code):
	from ast import literal_eval as le
	try:
		code.split()[1]
		imp = code.split()[1]
	except IndexError:
		imp = '*'
	try:
		fnd = le(open(code.split()[0] + '.cfbt').read())
	except FileNotFoundError:
		try:
			fnd = le(open('bullet/package/'+code.split()[0]+'/script.cfbt').read())
			for line in open('bullet/package/'+code.split()[0]+'/imports.txt'):
				line = line.replace('_PACKAGEDIR_','bullet/package/'+code.split()[0])
				imp_file(line)
		except FileNotFoundError:
			error('NoPackageError',f'No package named "{code.split()[0]}".')
			return True
	if imp == '*':
		for vn,vt in fnd['var'].items():
			var[vn] = vt
		for vn,vt in fnd['function'].items():
			vt['code'] = vt['code'].replace('%%ID6723087205QUOTE%%','"')
			function[vn] = vt
		try:
			function['__main__']
			main = True
		except KeyError:
			main = False
		if main:
			for line in function['__main__']['code'].splitlines():
				parse(line,d['atc'])
			del function['__main__']
	else:
		breakis = False
		try:
			data = fnd['var'][code.split()[1]]
			dt = 1
		except KeyError:
			try:
				data = fnd['function'][code.split()[1]]
				dt = 2
			except KeyError:
				error('ImportError',f'Can not import var or function {code.split()[1]} from {code.split()[0]}.')
				breakis = True
		if not breakis:
			if dt == 1:
				var[code.split()[1]] = data
			else:
				function[code.split()[1]] = data
def cf(code,d):
	from ast import literal_eval as le
	filename = d['fn']
	nf = ''
	filename = filename.replace('.bt','')
	for item in filename:
		nf += item
	filename = nf
	try:
		fnd = le(open(filename + '.cfbt').read())
	except FileNotFoundError:
		fnd = {'function':{},'var':{}}
	try:
		erase = code.split()[0]
	except KeyError:
		erase = 'True'
	if erase == 'True':
		fnd = {'function':{},'var':{}}
	for n,d in function.items():
		d['code'] = d['code'].replace('"','%%ID6723087205QUOTE%%').replace(';\n','\n')
		fnd['function'][n] = d
	for n,d in var.items():
		fnd['var'][n] = d
	open(filename + '.cfbt','w').write(str(fnd))
def ret(code):
	if d['funct'] != 'not':
		if (d['retd'] == 'not'):
			setvar('$' + d['funct'] + '.return',stringify(code,False),False)
		else:
			d['retd'] = stringify(code,False)
	else:
		error('ReturnError','Return can only be used inside functions.')
def error(et,er):
	try:
		eh[et]
		try:
			function[eh[et]]['attrib'][0]
			var[function[eh[et]]['attrib'][0]] = er
		except IndexError:
				pass
		if function[eh[et]]['attib'][0].startswith('event'):
				var[eh[et]]['event'] = {'type':et,'msg':er}
		for line in function[eh[et]]['code'].splitlines():
			parse(line,d['atc'])
	except KeyError:
		if '*' in eh.keys():
			if function[eh['*']]['attib'][0].startswith('event'):
				var[eh['*']]['event'] = {'type':et,'msg':er}
			for line in function[eh['*']]['code'].splitlines():
				parse(line,d['atc'])
		else:
			d['err'] = f'{et} triggered on line {str(d["count"]-1)} in file "{d["fn"]}": {er}'
def els(code):
	if d['else']:
		d['if'] = True
		d['em'] = 'else'
		if d['funct'] != 'not':
			d['close-count'] += 1
	else:
		d['if'] = False
def changestr(code):
	if code[0] == 'UPPER':
		code = code.replace('UPPER ','')
		if d['funct'] == 'not':
			var[d['prefix']+code] = var[d['prefix']+code].upper()
		else:
			var[d['funct']][d['prefix']+code] = var[d['funct']][d['prefix']+code].upper()
	elif code[0] == 'LOWER':
		code = code.replace('LOWER ','')
		if d['funct'] == 'not':
			var[d['prefix']+code] = var[d['prefix']+code].lower()
		else:
			var[d['funct']][d['prefix']+code] = var[d['funct']][d['prefix']+code].lower()
	elif code[0] == 'TITLE':
		code = code.replace('TITLE ','')
		if d['funct'] == 'not':
			var[d['prefix']+code] = var[d['prefix']+code].title()
		else:
			var[d['funct']][d['prefix']+code] = var[d['funct']][d['prefix']+code].title()
def WHILE(code):
	fnn = code.split(' & ')[1]
	cnd = code.split(' & ')[0]
	if 'no_while' in function[fnn]['head']:
		error('WhileError',f'While blocked by function header: "no_while" in function "{fnn}"')
		return True
	if 'no_loop' in function[fnn]['head']:
		error('WhileError',f'While blocked by function header: "no_loop" in function "{fnn}"')
		return True
	while eval(stringify(f"f'{cnd}'")):
		for line in function[fnn]['code'].splitlines():
			parse(line,d['atc'])
def foreach(code):
	fnn = code.split(' & ')[1]
	cnd = code.split(' & ')[0]
	if 'no_foreach' in function[fnn]['head']:
		error('ForeachError',f'Foreach blocked by function header: "no_foreach" in function "{fnn}"')
		return True
	if 'no_loop' in function[fnn]['head']:
		error('ForeachError',f'Foreach blocked by function header: "no_loop" in function "{fnn}"')
		return True
	if type(getvar(cnd)) == list:
		for item in getvar(cnd):
			var[function[fnn]['attrib'][0]] = item
			for line in function[fnn]['code'].splitlines():
				parse(line,d['atc'])
	elif type(getvar(cnd)) == dict:
		for z,o in getvar(cnd).items():
			var[function[fnn]['attrib'][0]] = z
			var[function[fnn]['attrib'][1]] = o
			for line in function[fnn]['code'].splitlines():
				parse(line,d['atc'])
	elif type(getvar(cnd)) == str:
		for item in getvar(cnd):
			var[function[fnn]['attrib'][0]] = item
			for line in function[fnn]['code'].splitlines():
				parse(line,d['atc'])
def isset(code):
	if d['funct'] == 'not':
		if code.split()[0] in var.keys():
			nret('ISSET','True')
		else:
			nret('ISSET','False')
	else:
		if code.split()[0] in var[d['funct']].keys():
			nret('ISSET','True')
		else:
			nret('ISSET','False')
def array_item(code):
	item = stringify(code.split(' & ')[1])
	try:
		item = int(item)
	except ValueError:
		pass
	lis = stringify(code.split(' & ')[0])
	nret('ARRAY_ITEM',lis[item])
def obj(code):
	from ast import literal_eval as le
	vn = code.split()[0]
	item = code.replace(vn+' = ','',1)
	if checkvn(vn):
		setvar(vn,le(item))
def err_h(code):
	eh[code.split(' & ')[0]] = code.split(' & ')[1]
def CLASS(code):
	if code == 'NULL':
		d['prefix'] = ''
	else:
		d['prefix'] = code+'.'
def rf(code):
	fnn = code.split()[0]
	for line in function[fnn]['code'].splitlines():
		parse(line,d['atc'])
def call_function(code,appendargs=[]):
	functname = code.split(' ')[0]
	strattrib = code.replace(functname+' ','',1)
	d['funct'] = d['prefix']+functname
	attrib = {}
	c = 0
	d['funct_lnc'] = 0
	appendargs = appendargs[::-1]
	var[functname] = {}
	if strattrib != '':
		for item in function[functname]['attrib']:
			if c == len(function[functname]['attrib'])-1:
				try:
					n = item.split('=')[0]
					opt = True
				except IndexError:
					n = item
					opt = False
				var[functname][n] = appendargs[len(function[functname]['attrib'])-len(appendargs)]
			else:
				try:
					try:
						n = item.split('=')[0]
						opt = True
					except IndexError:
						n = item
						opt = False
					var[functname][n] = stringify(strattrib.split(' & ')[c])
				except IndexError:
					if opt:
						try:
							var[functname][n] = stringify(item.split('=')[1])
						except IndexError:
							error('AttributeError',f'Missing required attribute "{item}".')
							return d['err']
					else:
						error('AttributeError',f'Missing required attribute "{item}".')
						return d['err']
			c += 1
	for line in function[functname]['code']:
		d['funct_lnc'] += 1
		parse(line,d['atc'])
def nret(loc,data,strnif=False):
	if strnif:
		data = stringify(data)
	if (d['retd'] == 'not'):
		setvar('$' + loc + '.return',data,False)
	else:
		d['retd'] = data
def sf(code):
	from ast import literal_eval as le
	if listify(code)[0] == ' ':
		code = code.replace(' ','',1)
	if listify(code.split('{')[0])[::-1][0] == ' ':
		code = code.split('{')[0][::-1].replace(' ','',1)[::-1] + '{' + code.split('{')[1]
	if code.startswith('{'):
		attrib = False
	else:
		attrib = True
	data = {'code':code.split('{')[1][::-1].replace('}','',1)[::-1],'head':[],'attrib':[],'sl':d['count']}
	if attrib:
		for attn in code.split('{')[0].split(' & '):
			data['attrib'].append(attn)
	retdt = str(data).replace("'",r"\'")
	nret('SHORT_FUNCTION',f"\\'{retdt}\\'")
def parse(code,atc):
	if atc == 'not':
		if d['if']:
			code = code.replace('\t','')
			err = ''
			try:
				cmd = code.split()[0]
			except IndexError:
				cmd = '//'
				code = '//'
			if cmd == 'OUT':
				code = code.replace('OUT ','',1)
				out(code)
				nret(cmd,'True')
			elif cmd.startswith('$'):
				#code = code.replace('VAR ','',1)
				vari(code)
				nret(cmd,'True')
			elif code.startswith('//'):
				pass
			elif cmd == 'ARRAY':
				code = code.replace('ARRAY ','',1)
				arr(code)
				nret(cmd,'True')
			elif cmd == 'INCLUDE':
				code = code.replace('INCLUDE ','',1)
				get(code)
				nret(cmd,'True')
			elif cmd == 'IN':
				code = code.replace('IN ','',1)
				IN(code)
				nret(cmd,'True')
			elif cmd == 'FUNCTION':
				code = code.replace('FUNCTION ','',1)
				fn(code)
				nret(cmd,'True')
			elif cmd == 'PYPARSE':
				code = code.replace('PYPARSE ','',1)
				parsepy(code)
				nret(cmd,'True')
			elif cmd == 'IF':
				code = code.replace('IF ','',1)
				IF(code)
			elif cmd == 'EVAL':
				code = code.replace('EVAL ','',1)
				EVAL(code)
			elif cmd == 'COMPILE':
				code = code.replace('COMPILE ','',1)
				cf(code,d)
			elif cmd == 'RETURN':
				code = code.replace('RETURN ','',1)
				ret(code)
			elif cmd == 'ELSE' or cmd == 'ELSE{':
				code = code.replace('ELSE ','',1)
				els(code)
			elif cmd == 'UPPER' or cmd == 'LOWER' or cmd == 'TITLE':
				changestr(code)
			elif cmd == 'WHILE':
				code = code.replace('WHILE ','',1)
				WHILE(code)
			elif cmd == 'FOREACH':
				code = code.replace('FOREACH ','',1)
				foreach(code)
			elif cmd == 'ISSET':
				code = code.replace('ISSET ','',1)
				isset(code)
			elif cmd == 'ARRAY_ITEM':
				code = code.replace('ARRAY_ITEM ','',1)
				array_item(code)
			elif cmd == 'OBJECT':
				code = code.replace('OBJECT ','',1)
				obj(code)
			elif cmd == 'SET_ERROR_HANDLER':
				code = code.replace('SET_ERROR_HANDLER ','',1)
				err_h(code)
			elif cmd == 'CLASS':
				code = code.replace('CLASS ','',1)
				CLASS(code)
			elif cmd == 'RUNFUNCTION':
				code = code.replace('RUNFUNCTION ','',1)
				rf(code)
			elif cmd.startswith('@'):
				code = code.replace('@','',1)
				d['sendto'] = code
			elif cmd == 'SHORT_FUNCTION' or cmd == 'SHORT_FUNCTION{':
				sf(code.replace('SHORT_FUNCTION','',1)[::-1].replace('}','',1)[::-1])
			else:
				callfunction(code)
			if err == '' and d['err'] == 'none':
				return True
			else:
				if err != '':
					return err
				else:
					return d['err']
		else:
			if code.startswith('}'):
				d['if'] = True
				if d['em'] == 'else':
					d['else'] = False
					d['em'] = 'none'
	else:
		err = ''
		if code.startswith('}') and d['close-count'] == 1:
			function[d['atc']]['code'] = function[d['atc']]['code'].replace(';','\n')
			oatc = d['atc']
			d['atc'] = 'not'
			if d['sendto'] != 'not':
				print(d['sendto']+' '+str(function[oatc]).replace(r'\n','BTCODE13561346543643653463nl'))
				callfunction(d['sendto']+' '+str(function[oatc]).replace(r'\n','BTCODE13561346543643653463nl'),True)
				'''functname = d['sendto'].split(' ')[0]
				strattrib = d['sendto'].replace(functname+' ','',1)
				attrib = {}
				c = 0
				var[functname] = {}
				if strattrib != '':
					for item in function[functname]['attrib']:
						if c == len(function[functname]['attrib'])-1:
							try:
								n = item.split('=')[0]
								opt = True
							except IndexError:
								n = item
								opt = False
							var[functname][n] = function[oatc]
						else:
							try:
								try:
									n = item.split('=')[0]
									opt = True
								except IndexError:
									n = item
									opt = False
								var[functname][n] = stringify(strattrib.split(' & ')[c])
							except IndexError:
								if opt:
									try:
										var[functname][n] = stringify(item.split('=')[1])
									except IndexError:
										error('AttributeError',f'Missing required attribute "{item}".')
										return d['err']
								else:
									error('AttributeError',f'Missing required attribute "{item}".')
									return d['err']
						c += 1
				for line in function[functname]['code']:
					parse(line,'not')'''
				d['sendto'] = 'not'
		else:
			d['close-count'] += charforeach('{',code)
			d['close-count'] -= charforeach('}',code)
			function[d['atc']]['code'] += code.replace('\n','').replace('\t','') + ';'
		if err == '' or d['err'] != '':
			return True
		else:
			if err != '':
				return err
			else:
				return d['err']
	return True
def start(d,count):
				count += 1
				d['count'] = count
				try:
					d['nl'] = open(d['fn']).readlines()[count]
				except IndexError:
					d['nl'] = 'nnl'
				da = parse(line,d['atc'])
				if not type(da) == bool:
					da = 'ERROR ' + da
					return da
					'''
				count += 1
				d['count'] = count
				if line.startswith('}'):
					d['if'] = True
					if d['em'] == 'else':
						d['else'] = False
						d['em'] = 'none'
						
				return count'''
				return count
try:
	open(d["fn"])
except FileNotFoundError:
	error('InvalidFileNameError',f'Invalid filename, "{d["fn"]}".')
ld = open('Bullet/UserPreferences/runonstart.bt').read()+'\n'+open(d["fn"]).read()
for line in open('Bullet/UserPreferences/autoinclude.txt'):
	get(line)
d['count'] = 0
count = 0
for line in ld.splitlines():
	count = start(d,count)
	if str(count).startswith('ERROR'):
		print(count.replace('ERROR ',''))
		break
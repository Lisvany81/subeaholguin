from pyobigram.utils import sizeof_fmt,nice_time
import datetime
import time
import os

def text_progres(index,max):
	try:
		if max<1:
			max += 1
		porcent = index / max
		porcent *= 100
		porcent = round(porcent)
		make_text = ''
		index_make = 1
		make_text += '\n'
		while(index_make<21):
			if porcent >= index_make * 5: make_text+='â'
			else: make_text+='â'
			index_make+=1
		make_text += '\n'
		return make_text
	except Exception as ex:
			return ''

def porcent(index,max):
    porcent = index / max
    porcent *= 100
    porcent = round(porcent)
    return porcent

def createDownloading(filename,totalBits,currentBits,speed,time,tid=''):
    msg = 'â¬  Descargando...\n'
    msg+= 'ð· Nombre: ' + str(filename)+'\n'
    msg+= 'ð¦ TamaÃ±o total: ' + str(sizeof_fmt(totalBits))+'\n'
    msg+= 'ð» Descargado: ' + str(sizeof_fmt(currentBits))+'\n'
    msg+= 'ð Velocidad: ' + str(sizeof_fmt(speed))+'/s\n'
    msg+= 'â° Tiempo: ' + str(datetime.timedelta(seconds=int(time))) +'\n\n'

    msg = 'â¬  Descargando...\n'
    msg += 'ð·  Archivo: '+filename+'\n'
    msg += text_progres(currentBits,totalBits)+'\n'
    msg += 'ð Progreso: '+str(porcent(currentBits,totalBits))+'%\n'
    msg += 'ð¦ TamaÃ±o total: '+sizeof_fmt(totalBits)+'\n'
    msg += 'ð» Descargado: '+sizeof_fmt(currentBits)+'\n'
    msg += 'ð Velocidad: '+sizeof_fmt(speed)+'/s\n'
    msg += 'â° Tiempo restante: '+str(datetime.timedelta(seconds=int(time)))+'s\n\n'

    if tid!='':
        msg+= '/cancel_' + tid
    return msg
def createUploading(filename,totalBits,currentBits,speed,time,originalname=''):
    msg = 'â¬ï¸ Subiendo...\n'
    msg+= 'ð· Nombre: ' + str(filename)+'\n'
    if originalname!='':
        msg = str(msg).replace(filename,originalname)
        msg+= 'â¬ï¸ Subiendo: ' + str(filename)+'\n'
    msg+= 'ð¦ TamaÃ±o total: ' + str(sizeof_fmt(totalBits))+'\n'
    msg+= 'ðº Subido: ' + str(sizeof_fmt(currentBits))+'\n'
    msg+= 'ð Velocidad: ' + str(sizeof_fmt(speed))+'/s\n'
    msg+= 'â° Tiempo: ' + str(datetime.timedelta(seconds=int(time))) +'\n'

    msg = 'â¬ï¸ Subiendo...\n'
    msg += 'ð· Nombre: '+filename+'\n'
    if originalname!='':
        msg = str(msg).replace(filename,originalname)
        msg+= 'ð Subiendo: ' + str(filename)+'\n'
    msg += text_progres(currentBits,totalBits)+'\n'
    msg += 'ð Progreso: '+str(porcent(currentBits,totalBits))+'%\n'
    msg += 'ð¦ TamaÃ±o total: '+sizeof_fmt(totalBits)+'\n'
    msg += 'ðº Subido: '+sizeof_fmt(currentBits)+'\n'
    msg += 'ð Velocidad: '+sizeof_fmt(speed)+'/s\n'
    msg += 'â° Tiempo restante: '+str(datetime.timedelta(seconds=int(time)))+'s\n\n'

    return msg
def createCompresing(filename,filesize,splitsize):
    msg = 'ð Comprimiendo...\n'
    msg+= 'ð· Nombre: ' + str(filename)+'\n'
    msg+= 'ð¦ TamaÃ±o total: ' + str(sizeof_fmt(filesize))+'\n'
    msg+= 'ð TamaÃ±o de partes: ' + str(sizeof_fmt(splitsize))+'\n'
    msg+= '#â£ Cantidad de partes: ' + str(round(int(filesize/splitsize)+1,1))+'\n\n'
    return msg
def createFinishUploading(filename,filesize,split_size,current,count,findex):
    msg = '<b>â Subida Completada</b>\n'
    msg+= 'ð· Nombre: ' + str(filename)+'\n'
    msg+= 'ð¦ TamaÃ±o total: ' + str(sizeof_fmt(filesize))+'\n'
    msg+= 'ð TamaÃ±o de partes: ' + str(sizeof_fmt(split_size))+'\n'
    msg+= '#â£ Cantidad de partes: ' + str(current) + '/' + str(count) +'\n\n'
    msg+= 'ð Borrar Archivo: ' + '/del_'+str(findex)
    return msg

def createFileMsg(filename,files):
    import urllib
    if len(files)>0:
        msg= '<b>ð Enlaces</b>\n'
        for f in files:
            url = urllib.parse.unquote(f['directurl'],encoding='utf-8', errors='replace')
            #msg+= '<a href="'+f['url']+'">' + f['name'] + '</a>'
            msg+= "<a href='"+url+"'>"+f['name']+'</a>\n'
        return msg
    return ''

def createFilesMsg(evfiles):
    msg = 'ð Archivos ('+str(len(evfiles))+') ð\n\n'
    i = 0
    for f in evfiles:
            try:
                fextarray = str(f['files'][0]['name']).split('.')
                fext = ''
                if len(fextarray)>=3:
                    fext = '.'+fextarray[-2]
                else:
                    fext = '.'+fextarray[-1]
                fname = f['name'] + fext
                msg+= '/txt_'+ str(i) + ' /del_'+ str(i) + '\n' + fname +'\n\n'
                i+=1
            except:pass
    return msg
def createStat(username,userdata,isadmin):
    from pyobigram.utils import sizeof_fmt
    msg = 'â ConfiguraciÃ³n de Usuario â\n\n'
    msg+= 'ð Nombre: @' + str(username)+'\n'
    msg+= 'ð¤ User: ' + str(userdata['moodle_user'])+'\n'
    msg+= 'ð Password: ' + str(userdata['moodle_password'])+'\n'
    msg+= 'ð Host: ' + str(userdata['moodle_host'])+'\n'
    if userdata['cloudtype'] == 'moodle':
        msg+= 'ð RepoID: ' + str(userdata['moodle_repo_id'])+'\n'
    msg+= 'â CloudType: ' + str(userdata['cloudtype'])+'\n'
    msg+= 'ð§° UpType: ' + str(userdata['uploadtype'])+'\n'
    if userdata['cloudtype'] == 'cloud':
        msg+= 'ð Dir: /' + str(userdata['dir'])+'\n'
    msg+= 'ð TamaÃ±o de Zips: ' + sizeof_fmt(userdata['zips']*1024*1024) + '\n\n'
    msgAdmin = 'NO'
    if isadmin:
        msgAdmin = 'SI'
    msg+= 'ð® Admin: ' + msgAdmin + '\n'
    proxy = 'NO'
    if userdata['proxy'] !='':
       proxy = 'SI'
    tokenize = 'NO'
    if userdata['tokenize']!=0:
       tokenize = 'SI'
    msg+= 'ð Proxy: ' + proxy + '\n'
    msg+= 'ð® Tokenize: ' + tokenize + '\n\n'
    msg+= 'â Configurar Moodle â\nð  Ejemplo /account user,password'
    return msg
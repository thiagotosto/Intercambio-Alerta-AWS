#retorna o template renderizado
#recebe dados para para renderizacao em forma de dicionario
def template_parser(data, template_file):
    with open(template_file, 'rw') as template:
        template_loader = template.read()
        template_loader = template_loader.replace('[ nome ]', data['nome'])

        if 'msg' in data.keys(): 
            template_loader = template_loader.replace('[ msg ]', data['msg'])
        return template_loader

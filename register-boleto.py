import logging.config

logging.config.dictConfig({
    'version': 1,
    'formatters': {
        'verbose': {
            'format': '%(name)s: %(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'zeep.transports': {
            'level': 'DEBUG',
            'propagate': True,
            'handlers': ['console'],
        },
    }
})

from sdk_bancodobrasil import Auth

from zeep import Client, Transport
from requests import Session

session = Session()
session.verify = './sdk_bancodobrasil/certificados/Autoridade_Certificadora_Raiz_Brasileira_v5.pem'
auth = Auth()
access_token = auth.get_access_token()
session.headers = {"Authorization": "Bearer {}".format(access_token)}

transport = Transport(session=session)

cli = Client(
    'https://cobranca.bb.com.br:7101/Processos/Ws/RegistroCobrancaService.serviceagent?wsdl',
    transport=transport
)
payload = {
    'numeroConvenio': 3170867,
    'numeroCarteira': 17,
    'numeroVariacaoCarteira': 19,
    'codigoModalidadeTitulo': 1,
    'dataEmissaoTitulo': '21.05.2019',
    'dataVencimentoTitulo': '23.05.2019',
    'indicadorPermissaoRecebimentoParcial': 'N',
    'nomePagador': 'RAPHAEL FILIPE SCHUBERT',
    'textoEnderecoPagador': 'R ISRAEL DE ALMEIDA',
    'nomeMunicipioPagador': 'ITAJAI',
    'nomeBairroPagador': 'SAO VICENTE',
    'siglaUfPagador': 'SC',
    'numeroCepPagador': 88312000,
    'valorOriginalTitulo': 1.99,
    'numeroInscricaoPagador': '07770374910',
    'codigoTipoInscricaoPagador': 1,
    'textoNumeroTituloCliente': '00031708670000000002',
    'codigoTipoTitulo': '4',
    'codigoTipoDesconto': '0',
    'codigoTipoJuroMora': 0,
    'codigoTipoMulta': 0,
    'codigoAceiteTitulo': 'A',
    'codigoChaveUsuario': 'JD028220',
    'codigoTipoCanalSolicitacao': 5,
}


print(cli.service.RegistroTituloCobranca(**payload))
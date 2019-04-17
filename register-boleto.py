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
session.verify = './sdk_bancodobrasil/certificados/AC_Banco_do_Brasil_v3_HOM.pem'
session.headers = {"Authorization": "Bearer {}".format(Auth().get_access_token())}
transport = Transport(session=session)

cli = Client(
    'https://cobranca.homologa.bb.com.br:7101/Processos/Ws/RegistroCobrancaService.serviceagent?wsdl',
    transport=transport
)
payload = {
    'numeroConvenio': 3170867,
    'numeroCarteira': 17,
    'numeroVariacaoCarteira': 19,
    'codigoModalidadeTitulo': 1,
    'dataEmissaoTitulo': '17.04.2019',
    'dataVencimentoTitulo': '17.04.2019',
    'indicadorPermissaoRecebimentoParcial': 'N',
    'nomePagador': 'RAPHAEL FILIPE SCHUBERT',
    'textoEnderecoPagador': 'R ISRAEL DE ALMEIDA',
    'nomeMunicipioPagador': 'ITAJAI',
    'nomeBairroPagador': 'SAO VICENTE',
    'siglaUfPagador': 'SC',
    'numeroCepPagador': 88312000,
    'valorOriginalTitulo': 1.99,
    'numeroInscricaoPagador': '73400584000166',
    'codigoTipoInscricaoPagador': 2,
    'textoNumeroTituloCliente': '00031708670000000001',
    'codigoTipoTitulo': '4',
    'codigoTipoDesconto': '0',
    'codigoTipoJuroMora': 0,
    'codigoTipoMulta': 0,
    'codigoAceiteTitulo': 'A',
    'codigoChaveUsuario': 'J1234567',
    'codigoTipoCanalSolicitacao': 5,
}


print(cli.service.RegistroTituloCobranca(**payload))
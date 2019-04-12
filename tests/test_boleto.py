from unittest import TestCase

from sdk_bancodobrasil import Boleto, BBBoletoBuilder


class BoletoTestCase(TestCase):

    def setUp(self):
        self.boleto = Boleto

    def test_emitir(self):
        self.boleto(prod=False).emitir()


class BBBoletoBuilderTestCase(TestCase):

    def setUp(self):
        self.boleto_builder = BBBoletoBuilder

    def test_check_fields_type(self):
        boleto_builder = self.boleto_builder({
            'numeroConvenio': 1000001,
            'numeroCarteira': '17',
            'numeroVariacaoCarteira': '019',
            'codigoModalidadeTITULO': '1',
            'dataEmissaoTITULO': '12.04.2019',
            'dataVencimentoTITULO': '12.04.2019',
            'valorOriginalTITULO': 1.99,
            'codigoTipoDesconto': '0',
            'codigoTipoJuroMora': 0,
            'codigoTipoMulta': 0,
            'codigoAceiteTITULO': 'A',
            'codigoTipoTITULO': '4',
            'indicadorPermissaoRecebimentoParcial': 'N',
            'textoNumeroTITULOCliente': '00012345670000000001',
            'codigoTipoInscricaoPagador': '1',
            'textoEnderecoPagador': 'R ISRAEL DE ALMEIDA',
            'numeroCepPagador': 88312000,
            'nomeMunicipioPagador': 'ITAJAI',
            'nomeBairroPagador': 'SAO VICENTE',
            'siglaUfPagador': 'SC',
            'codigoChaveUsuario': 'J1234567',
            'codigoTipoCanalSolicitacao': 5
        })
        self.assertEqual(boleto_builder.check_fields_type().valid, True)

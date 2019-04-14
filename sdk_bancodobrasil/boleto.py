import inspect
import os

from sdk_bancodobrasil import Auth
from validator import *


class BBBoletoBuilder:
    numeroConvenio = None
    numeroCarteira = None
    numeroVariacaoCarteira = None
    codigoModalidadeTITULO = None
    dataEmissaoTITULO = None
    dataVencimentoTITULO = None
    valorOriginalTITULO = None
    codigoTipoDesconto = None
    dataDescontoTITULO = None
    percentualDescontoTITULO = None
    valorDescontoTITULO = None
    valorAbatimentoTITULO = None
    quantidadeDiaProtesto = None
    codigoTipoJuroMora = None
    percentualJuroMoraTITULO = None
    valorJuroMoraTITULO = None
    codigoTipoMulta = None
    dataMultaTITULO = None
    percentualMultaTITULO = None
    valorMultaTITULO = None
    codigoAceiteTITULO = None
    codigoTipoTITULO = None
    textoDescricaoTipoTITULO = None
    indicadorPermissaoRecebimentoParcial = None
    textoNumeroTITULOBeneficiario = None
    textoCampoUtilizacaoBeneficiario = None
    codigoTipoContaCaucao = None
    textoNumeroTITULOCliente = None
    textoMensagemBloquetoOcorrencia = None
    codigoTipoInscricaoPagador = None
    numeroInscricaoPagador = None
    nomePagador = None
    textoEnderecoPagador = None
    numeroCepPagador = None
    nomeMunicipioPagador = None
    nomeBairroPagador = None
    siglaUfPagador = None
    textoNumeroTelefonePagador = None
    codigoTipoInscricaoAvalista = None
    numeroInscricaoAvalista = None
    nomeAvalistaTITULO = None
    codigoChaveUsuario = None
    codigoTipoCanalSolicitacao = None

    def __init__(self, dictionary={}, **kwargs):
        self.__dict__.update(dictionary)
        self.__dict__.update(kwargs)

    def check_fields_type(self):
        rules = {
            'numeroConvenio': [Required, InstanceOf(int), Range(1000000, 999999999)],
            'numeroCarteira': [Required, InstanceOf(str), Equals("17")],
            'numeroVariacaoCarteira': [Required, InstanceOf(str), Length(1, maximum=4)],
            'codigoModalidadeTITULO': [Required, InstanceOf(str), Equals("1")],
            'dataEmissaoTITULO': [Required, InstanceOf(str), Pattern("\d{2}\.\d{2}\.\d{4}")],
            'dataVencimentoTITULO': [Required, InstanceOf(str), Pattern("\d{2}\.\d{2}\.\d{4}")],
            'valorOriginalTITULO': [Required, InstanceOf(float)],
            'codigoTipoDesconto': [Required, InstanceOf(str), Length(1)],
            'dataDescontoTITULO': [InstanceOf(str), Pattern("\d{2}\.\d{2}\.\d{4}")],
            'percentualDescontoTITULO': [InstanceOf(float)],
            'valorDescontoTITULO': [InstanceOf(float)],
            'valorAbatimentoTITULO': [InstanceOf(float)],
            'quantidadeDiaProtesto': [InstanceOf(str), Length(1, maximum=4)],
            'codigoTipoJuroMora': [Required, InstanceOf(int)],
            'percentualJuroMoraTITULO': [InstanceOf(float)],
            'valorJuroMoraTITULO': [InstanceOf(float)],
            'codigoTipoMulta': [Required, InstanceOf(int), In([0, 1, 2])],
            'dataMultaTITULO': [InstanceOf(str), Pattern("\d{2}\.\d{2}\.\d{4}")],
            'percentualMultaTITULO': [InstanceOf(float)],
            'valorMultaTITULO': [InstanceOf(float)],
            'codigoAceiteTITULO': [Required, InstanceOf(str), Length(1)],
            'codigoTipoTITULO': [Required, InstanceOf(str), Length(1, maximum=4)],
            'textoDescricaoTipoTITULO': [InstanceOf(str), Length(1, maximum=30)],
            'indicadorPermissaoRecebimentoParcial': [Required, InstanceOf(str), In(["S", "N"])],
            'textoNumeroTITULOBeneficiario': [InstanceOf(str), Length(1, maximum=15)],
            'textoCampoUtilizacaoBeneficiario': [InstanceOf(str), Length(1, maximum=25)],
            'codigoTipoContaCaucao': [InstanceOf(int), Equals(0)],
            'textoNumeroTITULOCliente': [Required, InstanceOf(str), Length(1, maximum=20), Pattern("\d{3}\d{7}\d{10}")],
            'textoMensagemBloquetoOcorrencia': [InstanceOf(str), Length(1, maximum=220)],
            'codigoTipoInscricaoPagador': [Required, InstanceOf(str), Length(1), In(["1", "2"])],
            'numeroInscricaoPagador': [InstanceOf(int), Range(0, 999999999999999)],
            'nomePagador': [InstanceOf(str), Length(1, maximum=60)],
            'textoEnderecoPagador': [Required, InstanceOf(str), Length(1, maximum=60)],
            'numeroCepPagador': [Required, InstanceOf(int), Range(0, 99999999)],
            'nomeMunicipioPagador': [Required, InstanceOf(str), Length(1, maximum=20)],
            'nomeBairroPagador': [Required, InstanceOf(str), Length(1, maximum=20)],
            'siglaUfPagador': [Required, InstanceOf(str), Length(2)],
            'textoNumeroTelefonePagador': [InstanceOf(str), Length(1, maximum=12)],
            'codigoTipoInscricaoAvalista': [InstanceOf(str), Length(1), In(["1", "2"])],
            'numeroInscricaoAvalista': [InstanceOf(int), Range(0, 999999999999999)],
            'nomeAvalistaTITULO': [InstanceOf(str), Length(1, maximum=60)],
            'codigoChaveUsuario': [Required, InstanceOf(str), Length(8, maximum=8)],
            'codigoTipoCanalSolicitacao': [Required, InstanceOf(int), Equals(5)],
        }

        return validate(rules, self.__dict__)


class Boleto(Auth):

    def emitir(self, boleto: BBBoletoBuilder):
        base_path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        return

# -*- coding: utf-8 -*-

from django.test import TestCase
from django.contrib.gis.geos import Point

from ..models import Ponto, Avaliacao


class CreatePontoTest(TestCase):

    def setUp(self):
        ponto = Ponto(osmid=123, location=Point(1.34, 2.45))
        ponto.save()

    def test_str(self):
        self.assertEqual(Ponto.objects.get(osmid=123).__str__(),
                            str(Ponto.objects.get(osmid=123).id))


class CreateAvaliacaoTest(TestCase):

    def setUp(self):
        ponto1 = Ponto(osmid=123, location=Point(1.34, 2.45))
        ponto1.save()
        avaliacao_favoravel = Avaliacao(ponto=ponto1, acesso='favoravel',
            abrigo='favoravel', piso='favoravel', rampa='favoravel',
            calcada='favoravel', plataforma='favoravel',
            transito='favoravel', equipamento='favoravel',
            identificacao='critica', piso_tatil='critica',
            linhas='critica', logradouro='critica')
        avaliacao_favoravel.save()

        ponto2 = Ponto(osmid=234, location=Point(1.34, 2.45))
        ponto2.save()
        avaliacao_aceitavel = Avaliacao(ponto=ponto2, acesso='aceitavel',
            abrigo='aceitavel', piso='aceitavel', rampa='aceitavel',
            calcada='aceitavel', plataforma='aceitavel',
            transito='aceitavel', equipamento='aceitavel',
            identificacao='aceitavel', piso_tatil='aceitavel',
            linhas='aceitavel', logradouro='aceitavel')
        avaliacao_aceitavel.save()

        ponto3 = Ponto(osmid=345, location=Point(1.34, 2.45))
        ponto3.save()
        avaliacao_critica = Avaliacao(ponto=ponto3, acesso='aceitavel',
            abrigo='aceitavel', piso='aceitavel', rampa='aceitavel',
            calcada='aceitavel', plataforma='aceitavel',
            transito='aceitavel', equipamento='critica',
            identificacao='critica', piso_tatil='critica',
            linhas='critica', logradouro='critica')
        avaliacao_critica.save()

    def test_str(self):
        self.assertEqual(Avaliacao.objects.get(ponto__osmid=123).final(),
                            'favoravel')
        self.assertEqual(Avaliacao.objects.get(ponto__osmid=234).final(),
                            'aceitavel')
        self.assertEqual(Avaliacao.objects.get(ponto__osmid=345).final(),
                            'critica')
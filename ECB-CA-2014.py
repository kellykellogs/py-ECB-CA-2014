# -*- coding: utf-8 -*-
"""
Created on Sun Oct 26 17:19:00 2014

@author: Kelly
@version 0.1
"""
class CAResult(object):
     def __init__(self, value):
         self.NAME_OF_THE_ENTITY
         self.countrycode 
         self.A1= None
         self.A2= None
         self.A3= None
         self.A4= None
         self.A5= None
         self.A6= None
         self.A7= None
         self.A8= None
         self.A9= None
         self.A10= None
         self.A11= None
         self.A12= None
         self.B1= None
         self.B2= None
         self.B3= None
         self.B4= None
         self.B5= None
         self.B6= None
         self.B7= None
         self.B8= None
         self.B9= None
         self.B10= None
         self.B11= None
         self.C1= None
         self.C2= None
         self.C3= None
         self.C4= None
         self.C5= None
         self.C6= None
         self.C7= None
         self.D.A= None
         self.D.B= None
         self.D.C= None
         self.D.D= None
         self.D.E= None
         self.D.F= None
         self.D.G= None
         self.D.H= None
         self.D.I= None
         self.D10= None
         self.D11= None
         self.D12= None
         self.D13= None
         self.D20= None
         self.D21= None
         self.D22= None
         self.D23= None
         self.E.A= None
         self.E.B= None
         self.E.C= None
         self.E.D= None
         self.E.E= None
         self.E.F= None
         self.E.G= None
         self.E.H= None
         self.E.I= None
         self.E.J= None
         self.F1= None
         self.F2= None
         self.F3= None
     
        
     
     @property
     def Name(self):
          return self.Reference
     
     @Name.setter
     def Name(self,value):
          self.Reference= value
     
     
     @property
     def Total_Assets(self):
          return self.A1 
     
     @Total_Assets.setter
     def Total_Assets(self,value):
          self.A1 = value
     
     @property
     def Net_Profit_Loss_of_2013(self):
          return self.A2 
     
     @Net_Profit_Loss_of_2013.setter
     def Net_Profit_Loss_of_2013(self,value):
          self.A2 = value
     
     
     @property
     def Common_Equity_Tier_1_Capital(self):
          return self.A3
     
     @Common_Equity_Tier_1_Capital.setter
     def Common_Equity_Tier_1_Capital(self,value):
          self.A3= value
     
     
     @property
     def Total_risk_exposure(self):
          return self.A4
     
     @Total_risk_exposure.setter
     def Total_risk_exposure(self,value):
          self.A4= value
     
     
     @property
     def Total_exposure_measure_according_to_Article_429_CRR(self):
          return self.A5
     
     @Total_exposure_measure_according_to_Article_429_CRR.setter
     def Total_exposure_measure_according_to_Article_429_CRR(self,value):
          self.A5= value
     
     
     @property
     def CET1_ratio(self):
          return self.A6
     
     @CET1_ratio.setter
     def CET1_ratio(self,value):
          self.A6= value
     
     
     @property
     def Tier_1_Ratio(self):
          return self.A7
     
     @Tier_1_Ratio.setter
     def Tier_1_Ratio(self,value):
          self.A7= value
     
     
     @property
     def Core_Tier_one_ratio(self):
          return self.A8
     
     @Core_Tier_one_ratio.setter
     def Core_Tier_one_ratio(self,value):
          self.A8= value
     
     
     @property
     def Leverage_ratio_at_year_end_2013(self):
          return self.A9
     
     @Leverage_ratio_at_year_end_2013.setter
     def Leverage_ratio_at_year_end_2013(self,value):
          self.A9= value
     
     
     @property
     def Non_performing_exposures_ratio(self):
          return self.A10
     
     @Non_performing_exposures_ratio.setter
     def Non_performing_exposures_ratio(self,value):
          self.A10= value
     
     
     @property
     def Coverage_ratio_for_non_performing_exposure(self):
          return self.A11
     
     @Coverage_ratio_for_non_performing_exposure.setter
     def Coverage_ratio_for_non_performing_exposure(self,value):
          self.A11= value
     
     
     @property
     def Level_3_instruments_on_total_assets(self):
          return self.A12
     
     @Level_3_instruments_on_total_assets.setter
     def Level_3_instruments_on_total_assets(self,value):
          self.A12= value
     
     
     @property
     def CET1_Ratio(self):
          return self.B1
     
     @CET1_Ratio.setter
     def CET1_Ratio(self,value):
          self.B1= value
     
     
     @property
     def Aggregated_adjustments_due_to_the_outcome_of_the_AQR(self):
          return self.B2
     
     @Aggregated_adjustments_due_to_the_outcome_of_the_AQR.setter
     def Aggregated_adjustments_due_to_the_outcome_of_the_AQR(self,value):
          self.B2= value
     
     
     @property
     def _AQR_adjusted_CET1_Ratio(self):
          return self.B3
     
     @_AQR_adjusted_CET1_Ratio.setter
     def _AQR_adjusted_CET1_Ratio(self,value):
          self.B3= value
     
     
     @property
     def Aggregate_adjustments_due_to_the_outcome_of_the_baseline_scenario_of_the_joint_EBA_ECB_Stress_Test(self):
          return self.B4 
     
     @Aggregate_adjustments_due_to_the_outcome_of_the_baseline_scenario_of_the_joint_EBA_ECB_Stress_Test.setter
     def Aggregate_adjustments_due_to_the_outcome_of_the_baseline_scenario_of_the_joint_EBA_ECB_Stress_Test(self,value):
          self.B4 = value
     
     
     @property
     def Adjusted_CET1_Ratio_after_Baseline_Scenario(self):
          return self.B5
     
     @Adjusted_CET1_Ratio_after_Baseline_Scenario.setter
     def Adjusted_CET1_Ratio_after_Baseline_Scenario(self,value):
          self.B5= value
     
     
     @property
     def Aggregate_adjustments_due_to_the_outcome_of_the_adverse_scenario_of_the_joint_EBA_ECB_Stress_Test(self):
          return self.B6
     
     @Aggregate_adjustments_due_to_the_outcome_of_the_adverse_scenario_of_the_joint_EBA_ECB_Stress_Test.setter
     def Aggregate_adjustments_due_to_the_outcome_of_the_adverse_scenario_of_the_joint_EBA_ECB_Stress_Test(self,value):
          self.B6= value
     
     
     @property
     def Adjusted_CET1_Ratio_after_Adverse_Scenario(self):
          return self.B7
     
     @Adjusted_CET1_Ratio_after_Adverse_Scenario.setter
     def Adjusted_CET1_Ratio_after_Adverse_Scenario(self,value):
          self.B7= value
     
     
     @property
     def Shortfall_to_threshold_of_8prc_for_AQR_adjusted_CET1_Ratio(self):
          return self.B8
     
     @Shortfall_to_threshold_of_8prc_for_AQR_adjusted_CET1_Ratio.setter
     def Shortfall_to_threshold_of_8prc_for_AQR_adjusted_CET1_Ratio(self,value):
          self.B8= value
     
     
     @property
     def Shortfall_to_threshold_of_8prc_in_Baseline_Scenario(self):
          return self.B9
     
     @Shortfall_to_threshold_of_8prc_in_Baseline_Scenario.setter
     def Shortfall_to_threshold_of_8prc_in_Baseline_Scenario(self,value):
          self.B9= value
     
     
     @property
     def Shortfall_to_threshold_of_5p5prc_in_Adverse_Scenario(self):
          return self.B10
     
     @Shortfall_to_threshold_of_5p5prc_in_Adverse_Scenario.setter
     def Shortfall_to_threshold_of_5p5prc_in_Adverse_Scenario(self,value):
          self.B10= value
     
     
     @property
     def Aggregated_Capital_Shortfall_of_the_Comprehensive_Assessment(self):
          return self.B11
     
     @Aggregated_Capital_Shortfall_of_the_Comprehensive_Assessment.setter
     def Aggregated_Capital_Shortfall_of_the_Comprehensive_Assessment(self,value):
          self.B11= value
     
     
     @property
     def Raising_of_capital_instruments_eligible_as_CET1_capital(self):
          return self.C1
     
     @Raising_of_capital_instruments_eligible_as_CET1_capital.setter
     def Raising_of_capital_instruments_eligible_as_CET1_capital(self,value):
          self.C1= value
     
     
     @property
     def Repayment_of_CET1_capital_buybacks(self):
          return self.C2
     
     @Repayment_of_CET1_capital_buybacks.setter
     def Repayment_of_CET1_capital_buybacks(self,value):
          self.C2= value
     
     
     @property
     def Conversion_to_CET1_of_existing_hybrid_instruments(self):
          return self.C3
     
     @Conversion_to_CET1_of_existing_hybrid_instruments.setter
     def Conversion_to_CET1_of_existing_hybrid_instruments(self,value):
          self.C3= value
     
     
     @property
     def Net_Issuance_of_Additional_Tier_1_Instruments_with_a_trigger_at_or_above_5p5prc_and_below_6prc(self):
          return self.C4
     
     @Net_Issuance_of_Additional_Tier_1_Instruments_with_a_trigger_at_or_above_5p5prc_and_below_6prc.setter
     def Net_Issuance_of_Additional_Tier_1_Instruments_with_a_trigger_at_or_above_5p5prc_and_below_6prc(self,value):
          self.C4= value
     
     
     @property
     def Net_Issuance_of_Additional_Tier_1_Instruments_with_a_trigger_at_or_above_6prc_and_below_7prc(self):
          return self.C5
     
     @Net_Issuance_of_Additional_Tier_1_Instruments_with_a_trigger_at_or_above_6prc_and_below_7prc.setter
     def Net_Issuance_of_Additional_Tier_1_Instruments_with_a_trigger_at_or_above_6prc_and_below_7prc(self,value):
          self.C5= value
     
     
     @property
     def Net_Issuance_of_Additional_Tier_1_Instruments_with_a_trigger_at_or_above_7prc(self):
          return self.C6
     
     @Net_Issuance_of_Additional_Tier_1_Instruments_with_a_trigger_at_or_above_7prc.setter
     def Net_Issuance_of_Additional_Tier_1_Instruments_with_a_trigger_at_or_above_7prc(self,value):
          self.C6= value
     
     
     @property
     def Incurred_fines_litigation_costs_from_January_to_September_2014(self):
          return self.C7
     
     @Incurred_fines_litigation_costs_from_January_to_September_2014.setter
     def Incurred_fines_litigation_costs_from_January_to_September_2014(self,value):
          self.C7= value
     
     # under development
     
     
     @property
     def Leverage_Ratio_at_year_end_2013(self):
          return self.F1
     
     @Leverage_Ratio_at_year_end_2013.setter
     def Leverage_Ratio_at_year_end_2013(self,value):
          self.F1= value
     
     
     @property
     def Aggregated_adjustments_due_to_the_outcome_of_the_AQR(self):
          return self.F2
     
     @Aggregated_adjustments_due_to_the_outcome_of_the_AQR.setter
     def Aggregated_adjustments_due_to_the_outcome_of_the_AQR(self,value):
          self.F2= value
     
     
     @property
     def AQR_adjusted_Leverage_Ratio(self):
          return self.F3 
     
     @AQR_adjusted_Leverage_Ratio.setter
     def AQR_adjusted_Leverage_Ratio(self,value):
          self.F3 = value
     
     
     
#AT-BAWA-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'ATBAWA', '', u'BAWAG P.S.K. Bank f\xfcr Arbeit und Wirtschaft und \xd6sterreichische Postsp', '', '', '', '', '', '', '']


class entityATBAWA(CAResult):
     def __init__(self):
         self.shortname = "ATBAWA"
         self.origin = "AT-BAWA-CA-DISCLOSURE.xls"
         self.country = "AT"
         self.bank_specific_notes = "-"
         self.A1= 36472.0
         self.A1_dim= "Mill. EUR"
         self.A2= 245.0
         self.A2_dim= "Mill. EUR"
         self.A3= 2445.3703
         self.A3_dim= "Mill. EUR"
         self.A4= 16853.0
         self.A4_dim= "Mill. EUR"
         self.A5= 38098.0
         self.A5_dim= "Mill. EUR"
         self.A6= 0.1451
         self.A6_dim= "%"
         self.A7= 0.153
         self.A7_dim= "%"
         self.A8= 0.153079
         self.A8_dim= "%"
         self.A9= 0.0651
         self.A9_dim= "%"
         self.A10= 0.0261517103147
         self.A10_dim= "%"
         self.A11= 0.377473232287
         self.A11_dim= "%"
         self.A12= 0.000198
         self.A12_dim= "%"
         self.B1= 0.1451
         self.B1_dim= "%"
         self.B2= -20.9
         self.B2_dim= "Basis Points Change"
         self.B3= 0.14301
         self.B3_dim= "%"
         self.B4= -244.197982028
         self.B4_dim= "Basis Points Change"
         self.B5= 0.118590201797
         self.B5_dim= "%"
         self.B6= -575.977908477
         self.B6_dim= "Basis Points Change"
         self.B7= 0.0854122091523
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 363.8
         self.C2= -508.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#AT-ERST-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'ATERST', '', u'Erste Group Bank AG', '', '', '', '', '', '', '']


class entityATERST(CAResult):
     def __init__(self):
         self.shortname = "ATERST"
         self.origin = "AT-ERST-CA-DISCLOSURE.xls"
         self.country = "AT"
         self.bank_specific_notes = "N.B: The exposures referenced in the Fair Value asset review (Section D of Detailed AQR Results) include a number of cash assets and investment/foreclosed real estate assets. "
         self.A1= 197639.0
         self.A1_dim= "Mill. EUR"
         self.A2= 219.0
         self.A2_dim= "Mill. EUR"
         self.A3= 11276.3384
         self.A3_dim= "Mill. EUR"
         self.A4= 100952.0
         self.A4_dim= "Mill. EUR"
         self.A5= 221665.0
         self.A5_dim= "Mill. EUR"
         self.A6= 0.1117
         self.A6_dim= "%"
         self.A7= 0.118
         self.A7_dim= "%"
         self.A8= 0.11439
         self.A8_dim= "%"
         self.A9= 0.0519837978011
         self.A9_dim= "%"
         self.A10= 0.0565429835984
         self.A10_dim= "%"
         self.A11= 0.61230347966
         self.A11_dim= "%"
         self.A12= 0.00167477066773
         self.A12_dim= "%"
         self.B1= 0.1117
         self.B1_dim= "%"
         self.B2= -116.89
         self.B2_dim= "Basis Points Change"
         self.B3= 0.100011
         self.B3_dim= "%"
         self.B4= 11.8418650712
         self.B4_dim= "Basis Points Change"
         self.B5= 0.101195186507
         self.B5_dim= "%"
         self.B6= -242.203757736
         self.B6_dim= "Basis Points Change"
         self.B7= 0.0757906242264
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#AT-RANI-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'ATRANI', '', u'Raiffeisenlandesbank Nieder\xf6sterreich-Wien AG', '', '', '', '', '', '', '']


class entityATRANI(CAResult):
     def __init__(self):
         self.shortname = "ATRANI"
         self.origin = "AT-RANI-CA-DISCLOSURE.xls"
         self.country = "AT"
         self.bank_specific_notes = "-"
         self.A1= 29094.5712649
         self.A1_dim= "Mill. EUR"
         self.A2= 140.811364454
         self.A2_dim= "Mill. EUR"
         self.A3= 2279.434079
         self.A3_dim= "Mill. EUR"
         self.A4= 13010.447076
         self.A4_dim= "Mill. EUR"
         self.A5= 35136.8781821
         self.A5_dim= "Mill. EUR"
         self.A6= 0.175200288329
         self.A6_dim= "%"
         self.A7= 0.1162
         self.A7_dim= "%"
         self.A8= 0.172216
         self.A8_dim= "%"
         self.A9= 0.0649982069247
         self.A9_dim= "%"
         self.A10= 0.0204224411149
         self.A10_dim= "%"
         self.A11= 0.472969640136
         self.A11_dim= "%"
         self.A12= 0.008
         self.A12_dim= "%"
         self.B1= 0.175200288329
         self.B1_dim= "%"
         self.B2= -67.12
         self.B2_dim= "Basis Points Change"
         self.B3= 0.168488288329
         self.B3_dim= "%"
         self.B4= 16.246020045
         self.B4_dim= "Basis Points Change"
         self.B5= 0.170112890333
         self.B5_dim= "%"
         self.B6= -504.332311987
         self.B6_dim= "Basis Points Change"
         self.B7= 0.11805505713
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= -4.0

#AT-RAOB-CA_DISCLOSURE.xls
#

#AT-RAZE-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'ATRAZE', '', u'Raiffeisen Zentralbank \xd6sterreich AG', '', '', '', '', '', '', '']


class entityATRAZE(CAResult):
     def __init__(self):
         self.shortname = "ATRAZE"
         self.origin = "AT-RAZE-CA-DISCLOSURE.xls"
         self.country = "AT"
         self.bank_specific_notes = "-"
         self.A1= 147092.060504
         self.A1_dim= "Mill. EUR"
         self.A2= 614.431989
         self.A2_dim= "Mill. EUR"
         self.A3= 9483.9584
         self.A3_dim= "Mill. EUR"
         self.A4= 91544.0
         self.A4_dim= "Mill. EUR"
         self.A5= 165878.590032
         self.A5_dim= "Mill. EUR"
         self.A6= 0.1036
         self.A6_dim= "%"
         self.A7= 0.104
         self.A7_dim= "%"
         self.A8= 0.099307
         self.A8_dim= "%"
         self.A9= 0.0571467047015
         self.A9_dim= "%"
         self.A10= 0.0728383243969
         self.A10_dim= "%"
         self.A11= 0.642365547392
         self.A11_dim= "%"
         self.A12= 0.0032
         self.A12_dim= "%"
         self.B1= 0.1036
         self.B1_dim= "%"
         self.B2= -65.47
         self.B2_dim= "Basis Points Change"
         self.B3= 0.097053
         self.B3_dim= "%"
         self.B4= -22.809426027
         self.B4_dim= "Basis Points Change"
         self.B5= 0.0947720573973
         self.B5_dim= "%"
         self.B6= -193.716542708
         self.B6_dim= "Basis Points Change"
         self.B7= 0.0776813457292
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 2038.0
         self.C2= -2250.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#AT-VBH-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'ATVBH', '', u'\xd6sterreichische Volksbanken-AG with credit institutions affiliated acc', '', '', '', '', '', '', '']


class entityATVBH(CAResult):
     def __init__(self):
         self.shortname = "ATVBH"
         self.origin = "AT-VBH-CA-DISCLOSURE.xls"
         self.country = "AT"
         self.bank_specific_notes = "-"
         self.A1= 40602.1
         self.A1_dim= "Mill. EUR"
         self.A2= 5.6
         self.A2_dim= "Mill. EUR"
         self.A3= 3151.0
         self.A3_dim= "Mill. EUR"
         self.A4= 27451.0
         self.A4_dim= "Mill. EUR"
         self.A5= 45813.0
         self.A5_dim= "Mill. EUR"
         self.A6= 0.114786346581
         self.A6_dim= "%"
         self.A7= 0.1127
         self.A7_dim= "%"
         self.A8= 0.116214
         self.A8_dim= "%"
         self.A9= 0.0697
         self.A9_dim= "%"
         self.A10= 0.1072
         self.A10_dim= "%"
         self.A11= 0.4802
         self.A11_dim= "%"
         self.A12= 0.009
         self.A12_dim= "%"
         self.B1= 0.114786346581
         self.B1_dim= "%"
         self.B2= -115.44
         self.B2_dim= "Basis Points Change"
         self.B3= 0.103242346581
         self.B3_dim= "%"
         self.B4= -310.008705867
         self.B4_dim= "Basis Points Change"
         self.B5= 0.0722414759945
         self.B5_dim= "%"
         self.B6= -826.508119377
         self.B6_dim= "Basis Points Change"
         self.B7= 0.0205915346435
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 77.5887058672
         self.B10= 344.088119377
         self.B11= 344.088119377
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#BE-ABIG-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'BEABIG', '', u'Argenta Bank- en Verzekeringsgroep', '', '', '', '', '', '', '']


class entityBEABIG(CAResult):
     def __init__(self):
         self.shortname = "BEABIG"
         self.origin = "BE-ABIG-CA-DISCLOSURE.xls"
         self.country = "BE"
         self.bank_specific_notes = "-"
         self.A1= 36515.47
         self.A1_dim= "Mill. EUR"
         self.A2= 217.18
         self.A2_dim= "Mill. EUR"
         self.A3= 1387.985023
         self.A3_dim= "Mill. EUR"
         self.A4= 5715.541371
         self.A4_dim= "Mill. EUR"
         self.A5= 32678.83
         self.A5_dim= "Mill. EUR"
         self.A6= 0.242844016499
         self.A6_dim= "%"
         self.A7= 0.233402
         self.A7_dim= "%"
         self.A8= 0.223219
         self.A8_dim= "%"
         self.A9= 0.0424739808616
         self.A9_dim= "%"
         self.A10= 0.00870659908813
         self.A10_dim= "%"
         self.A11= 0.183946699695
         self.A11_dim= "%"
         self.A12= 0.0001
         self.A12_dim= "%"
         self.B1= 0.242844016499
         self.B1_dim= "%"
         self.B2= -18.87
         self.B2_dim= "Basis Points Change"
         self.B3= 0.240957016499
         self.B3_dim= "%"
         self.B4= -402.720100888
         self.B4_dim= "Basis Points Change"
         self.B5= 0.20068500641
         self.B5_dim= "%"
         self.B6= -938.55300482
         self.B6_dim= "Basis Points Change"
         self.B7= 0.147101716017
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#BE-AXA-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'BEAXA', '', u'AXA Bank Europe SA', '', '', '', '', '', '', '']


class entityBEAXA(CAResult):
     def __init__(self):
         self.shortname = "BEAXA"
         self.origin = "BE-AXA-CA-DISCLOSURE.xls"
         self.country = "BE"
         self.bank_specific_notes = "-"
         self.A1= 36885.75
         self.A1_dim= "Mill. EUR"
         self.A2= -12.22
         self.A2_dim= "Mill. EUR"
         self.A3= 794.352888
         self.A3_dim= "Mill. EUR"
         self.A4= 5225.489149
         self.A4_dim= "Mill. EUR"
         self.A5= 29886.425
         self.A5_dim= "Mill. EUR"
         self.A6= 0.152015029665
         self.A6_dim= "%"
         self.A7= 0.169087
         self.A7_dim= "%"
         self.A8= 0.169087
         self.A8_dim= "%"
         self.A9= 0.0275
         self.A9_dim= "%"
         self.A10= 0.0212236152532
         self.A10_dim= "%"
         self.A11= 0.457196452933
         self.A11_dim= "%"
         self.A12= 0.0
         self.A12_dim= "%"
         self.B1= 0.152015029665
         self.B1_dim= "%"
         self.B2= -53.59
         self.B2_dim= "Basis Points Change"
         self.B3= 0.146656029665
         self.B3_dim= "%"
         self.B4= -193.109471446
         self.B4_dim= "Basis Points Change"
         self.B5= 0.127345082521
         self.B5_dim= "%"
         self.B6= -1130.58838011
         self.B6_dim= "Basis Points Change"
         self.B7= 0.0335971916544
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 214.028380108
         self.B11= 214.028380108
         self.C1= 135.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 90.0
         self.C7= -0.9

#BE-BELF-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'BEBELF', '', u'Belfius Banque SA', '', '', '', '', '', '', '']


class entityBEBELF(CAResult):
     def __init__(self):
         self.shortname = "BEBELF"
         self.origin = "BE-BELF-CA-DISCLOSURE.xls"
         self.country = "BE"
         self.bank_specific_notes = "-"
         self.A1= 161072.0
         self.A1_dim= "Mill. EUR"
         self.A2= 445.0
         self.A2_dim= "Mill. EUR"
         self.A3= 7247.702192
         self.A3_dim= "Mill. EUR"
         self.A4= 52337.680936
         self.A4_dim= "Mill. EUR"
         self.A5= 211684.0
         self.A5_dim= "Mill. EUR"
         self.A6= 0.138479620464
         self.A6_dim= "%"
         self.A7= 0.153614
         self.A7_dim= "%"
         self.A8= 0.153614
         self.A8_dim= "%"
         self.A9= 0.0347
         self.A9_dim= "%"
         self.A10= 0.0182900611778
         self.A10_dim= "%"
         self.A11= 0.612568534308
         self.A11_dim= "%"
         self.A12= 0.0193814567398
         self.A12_dim= "%"
         self.B1= 0.138479620464
         self.B1_dim= "%"
         self.B2= -35.14
         self.B2_dim= "Basis Points Change"
         self.B3= 0.134965620464
         self.B3_dim= "%"
         self.B4= -251.291889408
         self.B4_dim= "Basis Points Change"
         self.B5= 0.109836431524
         self.B5_dim= "%"
         self.B6= -619.446951598
         self.B6_dim= "Basis Points Change"
         self.B7= 0.0730209253045
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#BE-BNY-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'BEBNY', '', u'The Bank of New York Mellon SA', '', '', '', '', '', '', '']


class entityBEBNY(CAResult):
     def __init__(self):
         self.shortname = "BEBNY"
         self.origin = "BE-BNY-CA-DISCLOSURE.xls"
         self.country = "BE"
         self.bank_specific_notes = "For this institution, the combined impact of the Asset Quality Review and the Join Up calculation is less than 10 basis points of RWA in the most extreme scenario year. This minor impact is displayed in this template, however the accompanying transparency template reflects the Stress Test data without taking this minor impact into account. Therefore, a small difference in CET1% end point between the two disclosure materials is to be expected. This template contains the official result."
         self.A1= 52901.0
         self.A1_dim= "Mill. EUR"
         self.A2= 134.0
         self.A2_dim= "Mill. EUR"
         self.A3= 1612.273135
         self.A3_dim= "Mill. EUR"
         self.A4= 10853.470378
         self.A4_dim= "Mill. EUR"
         self.A5= 61905.0
         self.A5_dim= "Mill. EUR"
         self.A6= 0.148549088803
         self.A6_dim= "%"
         self.A7= 0.178204
         self.A7_dim= "%"
         self.A8= 0.146509
         self.A8_dim= "%"
         self.A9= 0.026
         self.A9_dim= "%"
         self.A10= 0.0
         self.A10_dim= "%"
         self.A11= 0.0
         self.A11_dim= "%"
         self.A12= 0.0
         self.A12_dim= "%"
         self.B1= 0.148549088803
         self.B1_dim= "%"
         self.B2= -1.68
         self.B2_dim= "Basis Points Change"
         self.B3= 0.148381088803
         self.B3_dim= "%"
         self.B4= 6.71421566169
         self.B4_dim= "Basis Points Change"
         self.B5= 0.149052510369
         self.B5_dim= "%"
         self.B6= -360.764849854
         self.B6_dim= "Basis Points Change"
         self.B7= 0.112304603817
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#BE-DXIA-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'BEDXIA', '', u'Dexia NV', '', '', '', '', '', '', '']


class entityBEDXIA(CAResult):
     def __init__(self):
         self.shortname = "BEDXIA"
         self.origin = "BE-DXIA-CA-DISCLOSURE.xls"
         self.country = "BE"
         self.bank_specific_notes = "1. Taking into account the orderly resolution plan of this institution which benefits from a  State guarantee,  there is  no need to proceed with capital raising following CA results "
         self.A1= 222936.0
         self.A1_dim= "Mill. EUR"
         self.A2= -1081.0
         self.A2_dim= "Mill. EUR"
         self.A3= 8807.87724
         self.A3_dim= "Mill. EUR"
         self.A4= 53838.74002
         self.A4_dim= "Mill. EUR"
         self.A5= None
         self.A5_dim= "Mill. EUR"
         self.A6= 0.163597387991
         self.A6_dim= "%"
         self.A7= 0.2144
         self.A7_dim= "%"
         self.A8= 0.212397
         self.A8_dim= "%"
         self.A9= 0.0
         self.A9_dim= "%"
         self.A10= 0.0163241126276
         self.A10_dim= "%"
         self.A11= 0.376094791078
         self.A11_dim= "%"
         self.A12= 0.0513
         self.A12_dim= "%"
         self.B1= 0.163597387991
         self.B1_dim= "%"
         self.B2= -55.95
         self.B2_dim= "Basis Points Change"
         self.B3= 0.158002387991
         self.B3_dim= "%"
         self.B4= -502.916619211
         self.B4_dim= "Basis Points Change"
         self.B5= 0.10771072607
         self.B5_dim= "%"
         self.B6= -1084.97226705
         self.B6_dim= "Basis Points Change"
         self.B7= 0.0495051612863
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 54.9522670476
         self.B11= 54.9522670476
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#BE-KBC-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'BEKBC', '', u'KBC Group NV', '', '', '', '', '', '', '']


class entityBEKBC(CAResult):
     def __init__(self):
         self.shortname = "BEKBC"
         self.origin = "BE-KBC-CA-DISCLOSURE.xls"
         self.country = "BE"
         self.bank_specific_notes = 'Please note that -500 EUR MM (100%) of "Repayment of CET1 capital, buybacks" is already reflected in the Stress Test figures, and therefore should not be added to the post-Stress Test capital position, as this would constitute double-counting of capital raised.'
         self.A1= 241306.0
         self.A1_dim= "Mill. EUR"
         self.A2= 1014.937
         self.A2_dim= "Mill. EUR"
         self.A3= 12275.927582
         self.A3_dim= "Mill. EUR"
         self.A4= 92542.716653
         self.A4_dim= "Mill. EUR"
         self.A5= 260426.0
         self.A5_dim= "Mill. EUR"
         self.A6= 0.132651471947
         self.A6_dim= "%"
         self.A7= 0.158252
         self.A7_dim= "%"
         self.A8= 0.134971
         self.A8_dim= "%"
         self.A9= 0.0369
         self.A9_dim= "%"
         self.A10= 0.0669
         self.A10_dim= "%"
         self.A11= 0.4245
         self.A11_dim= "%"
         self.A12= 0.0173
         self.A12_dim= "%"
         self.B1= 0.132651471947
         self.B1_dim= "%"
         self.B2= -58.49
         self.B2_dim= "Basis Points Change"
         self.B3= 0.126802471947
         self.B3_dim= "%"
         self.B4= -65.7664104594
         self.B4_dim= "Basis Points Change"
         self.B5= 0.120225830901
         self.B5_dim= "%"
         self.B6= -441.302553635
         self.B6_dim= "Basis Points Change"
         self.B7= 0.0826722165835
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= -500.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#CY-BOCG-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'CYBOCG', '', u'Bank of Cyprus Public Company Ltd', '', '', '', '', '', '', '']


class entityCYBOCG(CAResult):
     def __init__(self):
         self.shortname = "CYBOCG"
         self.origin = "CY-BOCG-CA-DISCLOSURE.xls"
         self.country = "CY"
         self.bank_specific_notes = "-"
         self.A1= 29660.766
         self.A1_dim= "Mill. EUR"
         self.A2= -2138.178
         self.A2_dim= "Mill. EUR"
         self.A3= 2449.556972
         self.A3_dim= "Mill. EUR"
         self.A4= 23530.0
         self.A4_dim= "Mill. EUR"
         self.A5= 30628.0
         self.A5_dim= "Mill. EUR"
         self.A6= 0.104103568721
         self.A6_dim= "%"
         self.A7= 0.102
         self.A7_dim= "%"
         self.A8= 0.101665
         self.A8_dim= "%"
         self.A9= 0.08
         self.A9_dim= "%"
         self.A10= 0.4474
         self.A10_dim= "%"
         self.A11= 0.3408
         self.A11_dim= "%"
         self.A12= 0.00350756281884
         self.A12_dim= "%"
         self.B1= 0.104103568721
         self.B1_dim= "%"
         self.B2= -312.56
         self.B2_dim= "Basis Points Change"
         self.B3= 0.0728475687208
         self.B3_dim= "%"
         self.B4= 44.7926783274
         self.B4_dim= "Basis Points Change"
         self.B5= 0.0773268365535
         self.B5_dim= "%"
         self.B6= -577.958475746
         self.B6_dim= "Basis Points Change"
         self.B7= 0.0150517211462
         self.B7_dim= "%"
         self.B8= 71.52
         self.B9= 26.7273216726
         self.B10= 399.478475746
         self.B11= 399.478475746
         self.C1= 1000.0
         self.C2= None
         self.C3= None
         self.C4= None
         self.C5= None
         self.C6= None
         self.C7= None

#CY-CCBL-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'CYCCBL', '', u'Co-operative Central Bank Ltd', '', '', '', '', '', '', '']


class entityCYCCBL(CAResult):
     def __init__(self):
         self.shortname = "CYCCBL"
         self.origin = "CY-CCBL-CA-DISCLOSURE.xls"
         self.country = "CY"
         self.bank_specific_notes = "-"
         self.A1= 16294.0
         self.A1_dim= "Mill. EUR"
         self.A2= -1693.0
         self.A2_dim= "Mill. EUR"
         self.A3= -320.6568
         self.A3_dim= "Mill. EUR"
         self.A4= 8666.4
         self.A4_dim= "Mill. EUR"
         self.A5= 14183.0
         self.A5_dim= "Mill. EUR"
         self.A6= -0.037
         self.A6_dim= "%"
         self.A7= -0.0529
         self.A7_dim= "%"
         self.A8= -0.0529
         self.A8_dim= "%"
         self.A9= 0.0831
         self.A9_dim= "%"
         self.A10= 0.3991
         self.A10_dim= "%"
         self.A11= 0.3106
         self.A11_dim= "%"
         self.A12= 0.00110470111698
         self.A12_dim= "%"
         self.B1= -0.037
         self.B1_dim= "%"
         self.B2= -0.99
         self.B2_dim= "Basis Points Change"
         self.B3= -0.037099
         self.B3_dim= "%"
         self.B4= 47.0551610536
         self.B4_dim= "Basis Points Change"
         self.B5= -0.0323934838946
         self.B5_dim= "%"
         self.B6= -427.902139781
         self.B6_dim= "Basis Points Change"
         self.B7= -0.0798892139781
         self.B7_dim= "%"
         self.B8= 1170.99
         self.B9= 1123.93483895
         self.B10= 1348.89213978
         self.B11= 1348.89213978
         self.C1= 1500.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#CY-HB-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'CYHB', '', u'Hellenic Bank Public Company Ltd', '', '', '', '', '', '', '']


class entityCYHB(CAResult):
     def __init__(self):
         self.shortname = "CYHB"
         self.origin = "CY-HB-CA-DISCLOSURE.xls"
         self.country = "CY"
         self.bank_specific_notes = "-"
         self.A1= 6351.806
         self.A1_dim= "Mill. EUR"
         self.A2= -195.643
         self.A2_dim= "Mill. EUR"
         self.A3= 345.358805
         self.A3_dim= "Mill. EUR"
         self.A4= 4529.008602
         self.A4_dim= "Mill. EUR"
         self.A5= 7146.0
         self.A5_dim= "Mill. EUR"
         self.A6= 0.0762548352961
         self.A6_dim= "%"
         self.A7= 0.1312
         self.A7_dim= "%"
         self.A8= 0.0734
         self.A8_dim= "%"
         self.A9= 0.0679
         self.A9_dim= "%"
         self.A10= 0.2811
         self.A10_dim= "%"
         self.A11= 0.3705
         self.A11_dim= "%"
         self.A12= 0.00279521929577
         self.A12_dim= "%"
         self.B1= 0.0762548352961
         self.B1_dim= "%"
         self.B2= -240.34
         self.B2_dim= "Basis Points Change"
         self.B3= 0.0522208352961
         self.B3_dim= "%"
         self.B4= 95.0854531402
         self.B4_dim= "Basis Points Change"
         self.B5= 0.0617293806101
         self.B5_dim= "%"
         self.B6= -570.917560427
         self.B6_dim= "Basis Points Change"
         self.B7= -0.00487092074664
         self.B7_dim= "%"
         self.B8= 277.79
         self.B9= 182.70454686
         self.B10= 598.707560427
         self.B11= 598.707560427
         self.C1= None
         self.C2= None
         self.C3= 100.9
         self.C4= None
         self.C5= None
         self.C6= None
         self.C7= 0.0

#CY-RCB-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'CYRCB', '', u'RCB Bank Ltd', '', '', '', '', '', '', '']


class entityCYRCB(CAResult):
     def __init__(self):
         self.shortname = "CYRCB"
         self.origin = "CY-RCB-CA-DISCLOSURE.xls"
         self.country = "CY"
         self.bank_specific_notes = "-"
         self.A1= 8155.8
         self.A1_dim= "Mill. EUR"
         self.A2= 75.8
         self.A2_dim= "Mill. EUR"
         self.A3= 274.0
         self.A3_dim= "Mill. EUR"
         self.A4= 1645.0
         self.A4_dim= "Mill. EUR"
         self.A5= 8432.0
         self.A5_dim= "Mill. EUR"
         self.A6= 0.166565349544
         self.A6_dim= "%"
         self.A7= 0.166768
         self.A7_dim= "%"
         self.A8= 0.166768
         self.A8_dim= "%"
         self.A9= 0.0325441176471
         self.A9_dim= "%"
         self.A10= 0.0211
         self.A10_dim= "%"
         self.A11= 0.4428
         self.A11_dim= "%"
         self.A12= 0.0
         self.A12_dim= "%"
         self.B1= 0.166565349544
         self.B1_dim= "%"
         self.B2= 0.0
         self.B2_dim= "Basis Points Change"
         self.B3= 0.166565349544
         self.B3_dim= "%"
         self.B4= -96.0698439284
         self.B4_dim= "Basis Points Change"
         self.B5= 0.156958365151
         self.B5_dim= "%"
         self.B6= -501.887114327
         self.B6_dim= "Basis Points Change"
         self.B7= 0.116376638111
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#DE-AAB-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'DEAAB', '', u'Aareal Bank AG', '', '', '', '', '', '', '']


class entityDEAAB(CAResult):
     def __init__(self):
         self.shortname = "DEAAB"
         self.origin = "DE-AAB-CA-DISCLOSURE.xls"
         self.country = "DE"
         self.bank_specific_notes = "For this institution, the combined impact of the Asset Quality Review and the Join Up calculation is less than 10 basis points of RWA in the most extreme scenario year. This minor impact is displayed in this template, however the accompanying transparency template reflects the Stress Test data without taking this minor impact into account. Therefore, a small difference in CET1% end point between the two disclosure materials is to be expected. This template contains the official result."
         self.A1= 42982.0
         self.A1_dim= "Mill. EUR"
         self.A2= 136.0
         self.A2_dim= "Mill. EUR"
         self.A3= 2188.2289
         self.A3_dim= "Mill. EUR"
         self.A4= 13351.0
         self.A4_dim= "Mill. EUR"
         self.A5= 44221.0
         self.A5_dim= "Mill. EUR"
         self.A6= 0.1639
         self.A6_dim= "%"
         self.A7= 0.2077
         self.A7_dim= "%"
         self.A8= 0.173694
         self.A8_dim= "%"
         self.A9= 0.0463
         self.A9_dim= "%"
         self.A10= 0.031
         self.A10_dim= "%"
         self.A11= 0.2685
         self.A11_dim= "%"
         self.A12= 0.0
         self.A12_dim= "%"
         self.B1= 0.1639
         self.B1_dim= "%"
         self.B2= -10.33
         self.B2_dim= "Basis Points Change"
         self.B3= 0.162867
         self.B3_dim= "%"
         self.B4= 18.9403692494
         self.B4_dim= "Basis Points Change"
         self.B5= 0.164761036925
         self.B5_dim= "%"
         self.B6= -452.719670907
         self.B6_dim= "Basis Points Change"
         self.B7= 0.117595032909
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= -1.5

#DE-APAE-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'DEAPAE', '', u'Deutsche Apotheker- und \xc4rztebank eG', '', '', '', '', '', '', '']


class entityDEAPAE(CAResult):
     def __init__(self):
         self.shortname = "DEAPAE"
         self.origin = "DE-APAE-CA-DISCLOSURE.xls"
         self.country = "DE"
         self.bank_specific_notes = "Starting CET1 ratio displayed for year-end 2013 under 01.01.2014 regulations. May not exactly match EBA transparency template."
         self.A1= 34694.8
         self.A1_dim= "Mill. EUR"
         self.A2= 47.4
         self.A2_dim= "Mill. EUR"
         self.A3= 1751.440466
         self.A3_dim= "Mill. EUR"
         self.A4= 10593.384038
         self.A4_dim= "Mill. EUR"
         self.A5= 41500.0
         self.A5_dim= "Mill. EUR"
         self.A6= 0.165333425062
         self.A6_dim= "%"
         self.A7= 0.169763
         self.A7_dim= "%"
         self.A8= 0.181712
         self.A8_dim= "%"
         self.A9= 0.0424
         self.A9_dim= "%"
         self.A10= 0.0142
         self.A10_dim= "%"
         self.A11= 0.5424
         self.A11_dim= "%"
         self.A12= 0.0
         self.A12_dim= "%"
         self.B1= 0.165333425062
         self.B1_dim= "%"
         self.B2= -13.59
         self.B2_dim= "Basis Points Change"
         self.B3= 0.163974425062
         self.B3_dim= "%"
         self.B4= 88.3686867182
         self.B4_dim= "Basis Points Change"
         self.B5= 0.172811293734
         self.B5_dim= "%"
         self.B6= -174.478040678
         self.B6_dim= "Basis Points Change"
         self.B7= 0.146526620994
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 110.343
         self.C2= -9.217
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#DE-BLB-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'DEBLB', '', u'Bayerische Landesbank', '', '', '', '', '', '', '']


class entityDEBLB(CAResult):
     def __init__(self):
         self.shortname = "DEBLB"
         self.origin = "DE-BLB-CA-DISCLOSURE.xls"
         self.country = "DE"
         self.bank_specific_notes = "-"
         self.A1= 255836.0
         self.A1_dim= "Mill. EUR"
         self.A2= 124.0
         self.A2_dim= "Mill. EUR"
         self.A3= 13129.12125
         self.A3_dim= "Mill. EUR"
         self.A4= 93712.5
         self.A4_dim= "Mill. EUR"
         self.A5= 282452.0
         self.A5_dim= "Mill. EUR"
         self.A6= 0.1401
         self.A6_dim= "%"
         self.A7= 0.159
         self.A7_dim= "%"
         self.A8= 0.15309
         self.A8_dim= "%"
         self.A9= 0.0428
         self.A9_dim= "%"
         self.A10= 0.043
         self.A10_dim= "%"
         self.A11= 0.2706
         self.A11_dim= "%"
         self.A12= 0.0166
         self.A12_dim= "%"
         self.B1= 0.1401
         self.B1_dim= "%"
         self.B2= -81.94
         self.B2_dim= "Basis Points Change"
         self.B3= 0.131906
         self.B3_dim= "%"
         self.B4= -78.3929043446
         self.B4_dim= "Basis Points Change"
         self.B5= 0.124066709566
         self.B5_dim= "%"
         self.B6= -382.306940237
         self.B6_dim= "Basis Points Change"
         self.B7= 0.0936753059763
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#DE-COMM-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'DECOMM', '', u'Commerzbank AG', '', '', '', '', '', '', '']


class entityDECOMM(CAResult):
     def __init__(self):
         self.shortname = "DECOMM"
         self.origin = "DE-COMM-CA-DISCLOSURE.xls"
         self.country = "DE"
         self.bank_specific_notes = "-"
         self.A1= 561384.0
         self.A1_dim= "Mill. EUR"
         self.A2= 57.0
         self.A2_dim= "Mill. EUR"
         self.A3= 24587.0
         self.A3_dim= "Mill. EUR"
         self.A4= 215928.5
         self.A4_dim= "Mill. EUR"
         self.A5= 588953.0
         self.A5_dim= "Mill. EUR"
         self.A6= 0.113866395589
         self.A6_dim= "%"
         self.A7= 0.1349
         self.A7_dim= "%"
         self.A8= 0.134877
         self.A8_dim= "%"
         self.A9= 0.042033914421
         self.A9_dim= "%"
         self.A10= 0.035
         self.A10_dim= "%"
         self.A11= 0.4609
         self.A11_dim= "%"
         self.A12= 0.00391888618129
         self.A12_dim= "%"
         self.B1= 0.113866395589
         self.B1_dim= "%"
         self.B2= -54.97
         self.B2_dim= "Basis Points Change"
         self.B3= 0.108369395589
         self.B3_dim= "%"
         self.B4= 53.3003388108
         self.B4_dim= "Basis Points Change"
         self.B5= 0.11369942947
         self.B5_dim= "%"
         self.B6= -288.071100657
         self.B6_dim= "Basis Points Change"
         self.B7= 0.0795622855236
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#DE-DEBK-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'DEDEBK', '', u'Deutsche Bank AG', '', '', '', '', '', '', '']


class entityDEDEBK(CAResult):
     def __init__(self):
         self.shortname = "DEDEBK"
         self.origin = "DE-DEBK-CA-DISCLOSURE.xls"
         self.country = "DE"
         self.bank_specific_notes = "For this institution, the combined impact of the Asset Quality Review and the Join Up calculation is less than 10 basis points of RWA in the most extreme scenario year. This minor impact is displayed in this template, however the accompanying transparency template reflects the Stress Test data without taking this minor impact into account. Therefore, a small difference in CET1% end point between the two disclosure materials is to be expected. This template contains the official result."
         self.A1= 1580758.0
         self.A1_dim= "Mill. EUR"
         self.A2= 738.0
         self.A2_dim= "Mill. EUR"
         self.A3= 47311.81316
         self.A3_dim= "Mill. EUR"
         self.A4= 353102.861634
         self.A4_dim= "Mill. EUR"
         self.A5= 1444601.01605
         self.A5_dim= "Mill. EUR"
         self.A6= 0.133988755971
         self.A6_dim= "%"
         self.A7= 0.1688
         self.A7_dim= "%"
         self.A8= 0.128291
         self.A8_dim= "%"
         self.A9= 0.024
         self.A9_dim= "%"
         self.A10= 0.034958
         self.A10_dim= "%"
         self.A11= 0.409771251059
         self.A11_dim= "%"
         self.A12= 0.018
         self.A12_dim= "%"
         self.B1= 0.133988755971
         self.B1_dim= "%"
         self.B2= -6.83
         self.B2_dim= "Basis Points Change"
         self.B3= 0.133305755971
         self.B3_dim= "%"
         self.B4= -78.1043350621
         self.B4_dim= "Basis Points Change"
         self.B5= 0.125495322464
         self.B5_dim= "%"
         self.B6= -454.618482277
         self.B6_dim= "Basis Points Change"
         self.B7= 0.0878439077429
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 9784.0
         self.C2= 3.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= -1363.0

#DE-DEKA-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'DEDEKA', '', u'DekaBank Deutsche Girozentrale', '', '', '', '', '', '', '']


class entityDEDEKA(CAResult):
     def __init__(self):
         self.shortname = "DEDEKA"
         self.origin = "DE-DEKA-CA-DISCLOSURE.xls"
         self.country = "DE"
         self.bank_specific_notes = "-"
         self.A1= 116073.0
         self.A1_dim= "Mill. EUR"
         self.A2= 296.0
         self.A2_dim= "Mill. EUR"
         self.A3= 3642.8236
         self.A3_dim= "Mill. EUR"
         self.A4= 25708.0
         self.A4_dim= "Mill. EUR"
         self.A5= 98020.0
         self.A5_dim= "Mill. EUR"
         self.A6= 0.1417
         self.A6_dim= "%"
         self.A7= 0.1556
         self.A7_dim= "%"
         self.A8= 0.145
         self.A8_dim= "%"
         self.A9= 0.0396
         self.A9_dim= "%"
         self.A10= 0.0146
         self.A10_dim= "%"
         self.A11= 0.2282
         self.A11_dim= "%"
         self.A12= 0.0160088909566
         self.A12_dim= "%"
         self.B1= 0.1417
         self.B1_dim= "%"
         self.B2= -13.64
         self.B2_dim= "Basis Points Change"
         self.B3= 0.140336
         self.B3_dim= "%"
         self.B4= -177.633833547
         self.B4_dim= "Basis Points Change"
         self.B5= 0.122572616645
         self.B5_dim= "%"
         self.B6= -602.306267543
         self.B6_dim= "Basis Points Change"
         self.B7= 0.0801053732457
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#DE-DZB-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'DEDZB', '', u'DZ Bank AG Deutsche Zentral-Genossenschaftsbank', '', '', '', '', '', '', '']


class entityDEDZB(CAResult):
     def __init__(self):
         self.shortname = "DEDZB"
         self.origin = "DE-DZB-CA-DISCLOSURE.xls"
         self.country = "DE"
         self.bank_specific_notes = "-"
         self.A1= 315876.0
         self.A1_dim= "Mill. EUR"
         self.A2= 1385.0
         self.A2_dim= "Mill. EUR"
         self.A3= 9143.0
         self.A3_dim= "Mill. EUR"
         self.A4= 99760.0
         self.A4_dim= "Mill. EUR"
         self.A5= 407980.0
         self.A5_dim= "Mill. EUR"
         self.A6= 0.0916499599038
         self.A6_dim= "%"
         self.A7= 0.16389
         self.A7_dim= "%"
         self.A8= 0.14007
         self.A8_dim= "%"
         self.A9= 0.0274
         self.A9_dim= "%"
         self.A10= 0.0246
         self.A10_dim= "%"
         self.A11= 0.4324
         self.A11_dim= "%"
         self.A12= 0.0085
         self.A12_dim= "%"
         self.B1= 0.0916499599038
         self.B1_dim= "%"
         self.B2= -17.71
         self.B2_dim= "Basis Points Change"
         self.B3= 0.0898789599038
         self.B3_dim= "%"
         self.B4= -31.2274214643
         self.B4_dim= "Basis Points Change"
         self.B5= 0.0867562177573
         self.B5_dim= "%"
         self.B6= -301.616854406
         self.B6_dim= "Basis Points Change"
         self.B7= 0.0597172744632
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 1477.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#DE-HASP-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'DEHASP', '', u'HASPA Finanzholding', '', '', '', '', '', '', '']


class entityDEHASP(CAResult):
     def __init__(self):
         self.shortname = "DEHASP"
         self.origin = "DE-HASP-CA-DISCLOSURE.xls"
         self.country = "DE"
         self.bank_specific_notes = "-"
         self.A1= 44468.489
         self.A1_dim= "Mill. EUR"
         self.A2= 86.955
         self.A2_dim= "Mill. EUR"
         self.A3= 3933.37152
         self.A3_dim= "Mill. EUR"
         self.A4= 31517.4
         self.A4_dim= "Mill. EUR"
         self.A5= 51322.92
         self.A5_dim= "Mill. EUR"
         self.A6= 0.1248
         self.A6_dim= "%"
         self.A7= 0.1247
         self.A7_dim= "%"
         self.A8= 0.124711
         self.A8_dim= "%"
         self.A9= 0.0756
         self.A9_dim= "%"
         self.A10= 0.00976428364794
         self.A10_dim= "%"
         self.A11= 0.476410787667
         self.A11_dim= "%"
         self.A12= 0.0
         self.A12_dim= "%"
         self.B1= 0.1248
         self.B1_dim= "%"
         self.B2= -1.78
         self.B2_dim= "Basis Points Change"
         self.B3= 0.124622
         self.B3_dim= "%"
         self.B4= -2.70196080512
         self.B4_dim= "Basis Points Change"
         self.B5= 0.124351803919
         self.B5_dim= "%"
         self.B6= -172.509147373
         self.B6_dim= "Basis Points Change"
         self.B7= 0.107371085263
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#DE-HSH-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'DEHSH', '', u'HSH Nordbank AG', '', '', '', '', '', '', '']


class entityDEHSH(CAResult):
     def __init__(self):
         self.shortname = "DEHSH"
         self.origin = "DE-HSH-CA-DISCLOSURE.xls"
         self.country = "DE"
         self.bank_specific_notes = "- The increase in the Sunrise asset protection scheme from €7BN to €10BN in June 2013 was approved by DG Comp in 2013 as a rescue aid. Afterwards DG Comp initiated a state aid procedure. The rescue aid approval is valid until a final decision is reached in this ongoing procedure. The CA has been conducted on the basis of the fully €10BN. In case DG COMP will not finally approve the extension of the asset protection guarantee of 2013 this may create a capital shortfall for HSH against CA benchmarks. - Please note, as a result of the Capital Protection Clause for this institution reductions in CET1% below 10% are offset by corresponding reductions in the fair value of future premiums on the “Sunrise” guarantee scheme. Accordingly, the net AQR impact for this case is zero, despite AQR findings requiring additional provisions in individual portfolios."
         self.A1= 109279.0
         self.A1_dim= "Mill. EUR"
         self.A2= -870.0
         self.A2_dim= "Mill. EUR"
         self.A3= 3790.0
         self.A3_dim= "Mill. EUR"
         self.A4= 37900.0
         self.A4_dim= "Mill. EUR"
         self.A5= 118287.0
         self.A5_dim= "Mill. EUR"
         self.A6= 0.1
         self.A6_dim= "%"
         self.A7= 0.1533
         self.A7_dim= "%"
         self.A8= 0.116854
         self.A8_dim= "%"
         self.A9= 0.046
         self.A9_dim= "%"
         self.A10= 0.176750831077
         self.A10_dim= "%"
         self.A11= 0.3393169531
         self.A11_dim= "%"
         self.A12= 0.0318
         self.A12_dim= "%"
         self.B1= 0.1
         self.B1_dim= "%"
         self.B2= 0.0
         self.B2_dim= "Basis Points Change"
         self.B3= 0.1
         self.B3_dim= "%"
         self.B4= -58.6134494783
         self.B4_dim= "Basis Points Change"
         self.B5= 0.0941386550522
         self.B5_dim= "%"
         self.B6= -393.515237007
         self.B6_dim= "Basis Points Change"
         self.B7= 0.0606484762993
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#DE-HYMU-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'DEHYMU', '', u'M\xfcnchener Hypothekenbank eG', '', '', '', '', '', '', '']


class entityDEHYMU(CAResult):
     def __init__(self):
         self.shortname = "DEHYMU"
         self.origin = "DE-HYMU-CA-DISCLOSURE.xls"
         self.country = "DE"
         self.bank_specific_notes = "- For this institution, the combined impact of the Asset Quality Review and the Join Up calculation is less than 10 basis points of RWA in the most extreme scenario year. This minor impact is displayed in this template, however the accompanying transparency template reflects the Stress Test data without taking this minor impact into account. Therefore, a small difference in CET1% end point between the two disclosure materials is to be expected. This template contains the official result. - Starting CET1 ratio displayed for year-end 2013 under 01.01.2014 regulations. May not exactly match EBA transparency template."
         self.A1= 34899.0
         self.A1_dim= "Mill. EUR"
         self.A2= 48.06
         self.A2_dim= "Mill. EUR"
         self.A3= 531.64869
         self.A3_dim= "Mill. EUR"
         self.A4= 7738.7
         self.A4_dim= "Mill. EUR"
         self.A5= 36006.97
         self.A5_dim= "Mill. EUR"
         self.A6= 0.0687
         self.A6_dim= "%"
         self.A7= 0.1166
         self.A7_dim= "%"
         self.A8= 0.070324
         self.A8_dim= "%"
         self.A9= 0.0225
         self.A9_dim= "%"
         self.A10= 0.0115
         self.A10_dim= "%"
         self.A11= 0.1313
         self.A11_dim= "%"
         self.A12= 0.0
         self.A12_dim= "%"
         self.B1= 0.0687
         self.B1_dim= "%"
         self.B2= 0.0
         self.B2_dim= "Basis Points Change"
         self.B3= 0.0687
         self.B3_dim= "%"
         self.B4= -106.305722993
         self.B4_dim= "Basis Points Change"
         self.B5= 0.0580694277007
         self.B5_dim= "%"
         self.B6= -394.23143113
         self.B6_dim= "Basis Points Change"
         self.B7= 0.029276856887
         self.B7_dim= "%"
         self.B8= 113.0
         self.B9= 219.305722993
         self.B10= 257.23143113
         self.B11= 257.23143113
         self.C1= 350.53
         self.C2= -7.17
         self.C3= 64.75
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#DE-HYRE-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'DEHYRE', '', u'Hypo Real Estate Holding AG', '', '', '', '', '', '', '']


class entityDEHYRE(CAResult):
     def __init__(self):
         self.shortname = "DEHYRE"
         self.origin = "DE-HYRE-CA-DISCLOSURE.xls"
         self.country = "DE"
         self.bank_specific_notes = "-"
         self.A1= 122454.0
         self.A1_dim= "Mill. EUR"
         self.A2= 160.0
         self.A2_dim= "Mill. EUR"
         self.A3= 4086.3796
         self.A3_dim= "Mill. EUR"
         self.A4= 24484.0
         self.A4_dim= "Mill. EUR"
         self.A5= 110228.0
         self.A5_dim= "Mill. EUR"
         self.A6= 0.1669
         self.A6_dim= "%"
         self.A7= 0.3245
         self.A7_dim= "%"
         self.A8= 0.241484
         self.A8_dim= "%"
         self.A9= 0.0423
         self.A9_dim= "%"
         self.A10= 0.0087
         self.A10_dim= "%"
         self.A11= 0.1867
         self.A11_dim= "%"
         self.A12= 0.0013
         self.A12_dim= "%"
         self.B1= 0.1669
         self.B1_dim= "%"
         self.B2= -15.1
         self.B2_dim= "Basis Points Change"
         self.B3= 0.16539
         self.B3_dim= "%"
         self.B4= 161.673825604
         self.B4_dim= "Basis Points Change"
         self.B5= 0.18155738256
         self.B5_dim= "%"
         self.B6= -576.237435074
         self.B6_dim= "Basis Points Change"
         self.B7= 0.107766256493
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#DE-IKB-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'DEIKB', '', u'IKB Deutsche Industriebank AG', '', '', '', '', '', '', '']


class entityDEIKB(CAResult):
     def __init__(self):
         self.shortname = "DEIKB"
         self.origin = "DE-IKB-CA-DISCLOSURE.xls"
         self.country = "DE"
         self.bank_specific_notes = "-"
         self.A1= 24705.67
         self.A1_dim= "Mill. EUR"
         self.A2= 440.0
         self.A2_dim= "Mill. EUR"
         self.A3= 1340.992873
         self.A3_dim= "Mill. EUR"
         self.A4= 14327.0
         self.A4_dim= "Mill. EUR"
         self.A5= 24373.0
         self.A5_dim= "Mill. EUR"
         self.A6= 0.093599
         self.A6_dim= "%"
         self.A7= 0.130807
         self.A7_dim= "%"
         self.A8= 0.096649
         self.A8_dim= "%"
         self.A9= 0.074265
         self.A9_dim= "%"
         self.A10= 0.0458298006491
         self.A10_dim= "%"
         self.A11= 0.41107738419
         self.A11_dim= "%"
         self.A12= 0.0
         self.A12_dim= "%"
         self.B1= 0.093599
         self.B1_dim= "%"
         self.B2= -31.15
         self.B2_dim= "Basis Points Change"
         self.B3= 0.090484
         self.B3_dim= "%"
         self.B4= -36.2275891362
         self.B4_dim= "Basis Points Change"
         self.B5= 0.0868612410864
         self.B5_dim= "%"
         self.B6= -252.00673323
         self.B6_dim= "Basis Points Change"
         self.B7= 0.065283326677
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= -1.0

#DE-KFW-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'DEKFW', '', u'KfW IPEX-Bank GmbH', '', '', '', '', '', '', '']


class entityDEKFW(CAResult):
     def __init__(self):
         self.shortname = "DEKFW"
         self.origin = "DE-KFW-CA-DISCLOSURE.xls"
         self.country = "DE"
         self.bank_specific_notes = "Starting CET1 ratio displayed for year-end 2013 under 01.01.2014 regulations. May not exactly match EBA transparency template."
         self.A1= 23437.0
         self.A1_dim= "Mill. EUR"
         self.A2= 85.0
         self.A2_dim= "Mill. EUR"
         self.A3= 2451.608418
         self.A3_dim= "Mill. EUR"
         self.A4= 18614.0
         self.A4_dim= "Mill. EUR"
         self.A5= 32148.0
         self.A5_dim= "Mill. EUR"
         self.A6= 0.131707769313
         self.A6_dim= "%"
         self.A7= 0.1845
         self.A7_dim= "%"
         self.A8= 0.130225
         self.A8_dim= "%"
         self.A9= 0.073
         self.A9_dim= "%"
         self.A10= 0.0515
         self.A10_dim= "%"
         self.A11= 0.5812
         self.A11_dim= "%"
         self.A12= 0.0
         self.A12_dim= "%"
         self.B1= 0.131707769313
         self.B1_dim= "%"
         self.B2= -37.21
         self.B2_dim= "Basis Points Change"
         self.B3= 0.127986769313
         self.B3_dim= "%"
         self.B4= -82.5649445015
         self.B4_dim= "Basis Points Change"
         self.B5= 0.119730274863
         self.B5_dim= "%"
         self.B6= -338.303631746
         self.B6_dim= "Basis Points Change"
         self.B7= 0.0941564061389
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#DE-LBB-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'DELBB', '', u'Landesbank Berlin Holding AG', '', '', '', '', '', '', '']


class entityDELBB(CAResult):
     def __init__(self):
         self.shortname = "DELBB"
         self.origin = "DE-LBB-CA-DISCLOSURE.xls"
         self.country = "DE"
         self.bank_specific_notes = "-"
         self.A1= 101157.0
         self.A1_dim= "Mill. EUR"
         self.A2= 233.0
         self.A2_dim= "Mill. EUR"
         self.A3= 3112.0
         self.A3_dim= "Mill. EUR"
         self.A4= 31207.0
         self.A4_dim= "Mill. EUR"
         self.A5= 88400.0
         self.A5_dim= "Mill. EUR"
         self.A6= 0.0997212163938
         self.A6_dim= "%"
         self.A7= 0.1145
         self.A7_dim= "%"
         self.A8= 0.106939
         self.A8_dim= "%"
         self.A9= 0.036
         self.A9_dim= "%"
         self.A10= 0.0216684184948
         self.A10_dim= "%"
         self.A11= 0.366283056501
         self.A11_dim= "%"
         self.A12= 0.0016
         self.A12_dim= "%"
         self.B1= 0.0997212163938
         self.B1_dim= "%"
         self.B2= -8.02
         self.B2_dim= "Basis Points Change"
         self.B3= 0.0989192163938
         self.B3_dim= "%"
         self.B4= 23.7918574525
         self.B4_dim= "Basis Points Change"
         self.B5= 0.101298402139
         self.B5_dim= "%"
         self.B6= -306.109830793
         self.B6_dim= "Basis Points Change"
         self.B7= 0.0683082333145
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#DE-LBW-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'DELBW', '', u'Landesbank Baden-W\xfcrttemberg', '', '', '', '', '', '', '']


class entityDELBW(CAResult):
     def __init__(self):
         self.shortname = "DELBW"
         self.origin = "DE-LBW-CA-DISCLOSURE.xls"
         self.country = "DE"
         self.bank_specific_notes = "-"
         self.A1= 273523.0
         self.A1_dim= "Mill. EUR"
         self.A2= 337.0
         self.A2_dim= "Mill. EUR"
         self.A3= 12358.991382
         self.A3_dim= "Mill. EUR"
         self.A4= 88441.0
         self.A4_dim= "Mill. EUR"
         self.A5= 294923.0
         self.A5_dim= "Mill. EUR"
         self.A6= 0.13974278199
         self.A6_dim= "%"
         self.A7= 0.1805
         self.A7_dim= "%"
         self.A8= 0.160333
         self.A8_dim= "%"
         self.A9= 0.047
         self.A9_dim= "%"
         self.A10= 0.0183124757027
         self.A10_dim= "%"
         self.A11= 0.398918846881
         self.A11_dim= "%"
         self.A12= 0.0081
         self.A12_dim= "%"
         self.B1= 0.13974278199
         self.B1_dim= "%"
         self.B2= -50.36
         self.B2_dim= "Basis Points Change"
         self.B3= 0.13470678199
         self.B3_dim= "%"
         self.B4= -118.38017306
         self.B4_dim= "Basis Points Change"
         self.B5= 0.122868764684
         self.B5_dim= "%"
         self.B6= -604.711341955
         self.B6_dim= "Basis Points Change"
         self.B7= 0.0742356477947
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= -1.0

#DE-LHTG-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'DELHTG', '', u'Landesbank Hessen-Th\xfcringen Girozentrale', '', '', '', '', '', '', '']


class entityDELHTG(CAResult):
     def __init__(self):
         self.shortname = "DELHTG"
         self.origin = "DE-LHTG-CA-DISCLOSURE.xls"
         self.country = "DE"
         self.bank_specific_notes = "-"
         self.A1= 176999.0
         self.A1_dim= "Mill. EUR"
         self.A2= 353.0
         self.A2_dim= "Mill. EUR"
         self.A3= 7065.0
         self.A3_dim= "Mill. EUR"
         self.A4= 56531.0
         self.A4_dim= "Mill. EUR"
         self.A5= 193711.0
         self.A5_dim= "Mill. EUR"
         self.A6= 0.124975677062
         self.A6_dim= "%"
         self.A7= 0.127647
         self.A7_dim= "%"
         self.A8= 0.115227
         self.A8_dim= "%"
         self.A9= 0.0388
         self.A9_dim= "%"
         self.A10= 0.0251889803725
         self.A10_dim= "%"
         self.A11= 0.261246222768
         self.A11_dim= "%"
         self.A12= 0.0032
         self.A12_dim= "%"
         self.B1= 0.124975677062
         self.B1_dim= "%"
         self.B2= -26.88
         self.B2_dim= "Basis Points Change"
         self.B3= 0.122287677062
         self.B3_dim= "%"
         self.B4= -78.8979562128
         self.B4_dim= "Basis Points Change"
         self.B5= 0.114397881441
         self.B5_dim= "%"
         self.B6= -406.535130825
         self.B6_dim= "Basis Points Change"
         self.B7= 0.0816341639796
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= -18.0

#DE-LKBW-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'DELKBW', '', u'Landeskreditbank Baden-W\xfcrttemberg-F\xf6rderbank', '', '', '', '', '', '', '']


class entityDELKBW(CAResult):
     def __init__(self):
         self.shortname = "DELKBW"
         self.origin = "DE-LKBW-CA-DISCLOSURE.xls"
         self.country = "DE"
         self.bank_specific_notes = "For this institution, the combined impact of the Asset Quality Review and the Join Up calculation is less than 10 basis points of RWA in the most extreme scenario year. This minor impact is displayed in this template, however the accompanying transparency template reflects the Stress Test data without taking this minor impact into account. Therefore, a small difference in CET1% end point between the two disclosure materials is to be expected. This template contains the official result."
         self.A1= 70682.0
         self.A1_dim= "Mill. EUR"
         self.A2= 101.0
         self.A2_dim= "Mill. EUR"
         self.A3= 2933.040875
         self.A3_dim= "Mill. EUR"
         self.A4= 21737.5
         self.A4_dim= "Mill. EUR"
         self.A5= 79304.0
         self.A5_dim= "Mill. EUR"
         self.A6= 0.13493
         self.A6_dim= "%"
         self.A7= 0.166
         self.A7_dim= "%"
         self.A8= 0.16594
         self.A8_dim= "%"
         self.A9= 0.037
         self.A9_dim= "%"
         self.A10= 0.0118
         self.A10_dim= "%"
         self.A11= 0.737
         self.A11_dim= "%"
         self.A12= 0.0
         self.A12_dim= "%"
         self.B1= 0.13493
         self.B1_dim= "%"
         self.B2= 0.0
         self.B2_dim= "Basis Points Change"
         self.B3= 0.13493
         self.B3_dim= "%"
         self.B4= 33.057165719
         self.B4_dim= "Basis Points Change"
         self.B5= 0.138235716572
         self.B5_dim= "%"
         self.B6= -227.479963596
         self.B6_dim= "Basis Points Change"
         self.B7= 0.11218200364
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 49.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#DE-LWREB-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'DELWREB', '', u'Landwirtschaftliche Rentenbank', '', '', '', '', '', '', '']


class entityDELWREB(CAResult):
     def __init__(self):
         self.shortname = "DELWREB"
         self.origin = "DE-LWREB-CA-DISCLOSURE.xls"
         self.country = "DE"
         self.bank_specific_notes = "- For this institution, the combined impact of the Asset Quality Review and the Join Up calculation is less than 10 basis points of RWA in the most extreme scenario year. This minor impact is displayed in this template, however the accompanying transparency template reflects the Stress Test data without taking this minor impact into account. Therefore, a small difference in CET1% end point between the two disclosure materials is to be expected. This template contains the official result. - The Asset Quality Review for this institution constituted a targeted review of exposures to other Financial Institutions. "
         self.A1= 81932.0
         self.A1_dim= "Mill. EUR"
         self.A2= 460.0
         self.A2_dim= "Mill. EUR"
         self.A3= 2906.856
         self.A3_dim= "Mill. EUR"
         self.A4= 17180.0
         self.A4_dim= "Mill. EUR"
         self.A5= 81346.0
         self.A5_dim= "Mill. EUR"
         self.A6= 0.1692
         self.A6_dim= "%"
         self.A7= 0.2391
         self.A7_dim= "%"
         self.A8= 0.239114
         self.A8_dim= "%"
         self.A9= 0.0357
         self.A9_dim= "%"
         self.A10= 0.0
         self.A10_dim= "%"
         self.A11= 0.0
         self.A11_dim= "%"
         self.A12= 0.0458917150808
         self.A12_dim= "%"
         self.B1= 0.1692
         self.B1_dim= "%"
         self.B2= -3.9
         self.B2_dim= "Basis Points Change"
         self.B3= 0.16881
         self.B3_dim= "%"
         self.B4= -76.7016975289
         self.B4_dim= "Basis Points Change"
         self.B5= 0.161139830247
         self.B5_dim= "%"
         self.B6= -398.70454322
         self.B6_dim= "Basis Points Change"
         self.B7= 0.128939545678
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#DE-NLG-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'DENLG', '', u'Norddeutsche Landesbank-Girozentrale', '', '', '', '', '', '', '']


class entityDENLG(CAResult):
     def __init__(self):
         self.shortname = "DENLG"
         self.origin = "DE-NLG-CA-DISCLOSURE.xls"
         self.country = "DE"
         self.bank_specific_notes = "Please note: the AQR-adjusted CET1 Ratio (item B3 in the sheet ‘Main Results and Overview’) includes both the impact of the AQR, and an adjustment due to IRB provisioning shortfall. The IRB provisioning shortfall adjustment is not presented in the sheet ‘Detailed AQR Results’. "
         self.A1= 197662.97
         self.A1_dim= "Mill. EUR"
         self.A2= 280.01451713
         self.A2_dim= "Mill. EUR"
         self.A3= 7760.4
         self.A3_dim= "Mill. EUR"
         self.A4= 73089.5
         self.A4_dim= "Mill. EUR"
         self.A5= 218238.039
         self.A5_dim= "Mill. EUR"
         self.A6= 0.106176673804
         self.A6_dim= "%"
         self.A7= 0.1185
         self.A7_dim= "%"
         self.A8= 0.118475
         self.A8_dim= "%"
         self.A9= 0.0344
         self.A9_dim= "%"
         self.A10= 0.0354896515454
         self.A10_dim= "%"
         self.A11= 0.292816011293
         self.A11_dim= "%"
         self.A12= 0.00209899575429
         self.A12_dim= "%"
         self.B1= 0.106176673804
         self.B1_dim= "%"
         self.B2= -48.6657394204
         self.B2_dim= "Basis Points Change"
         self.B3= 0.101310099862
         self.B3_dim= "%"
         self.B4= 80.3616750337
         self.B4_dim= "Basis Points Change"
         self.B5= 0.109346267365
         self.B5_dim= "%"
         self.B6= -136.140604865
         self.B6_dim= "Basis Points Change"
         self.B7= 0.0876960393755
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#DE-NRW-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'DENRW', '', u'NRW.Bank', '', '', '', '', '', '', '']


class entityDENRW(CAResult):
     def __init__(self):
         self.shortname = "DENRW"
         self.origin = "DE-NRW-CA-DISCLOSURE.xls"
         self.country = "DE"
         self.bank_specific_notes = "- For this institution, the combined impact of the Asset Quality Review and the Join Up calculation is less than 10 basis points of RWA in the most extreme scenario year. This minor impact is displayed in this template, however the accompanying transparency template reflects the Stress Test data without taking this minor impact into account. Therefore, a small difference in CET1% end point between the two disclosure materials is to be expected. This template contains the official result. - Starting CET1 ratio displayed for year-end 2013 under 01.01.2014 regulations. May not exactly match EBA transparency template."
         self.A1= 145350.0
         self.A1_dim= "Mill. EUR"
         self.A2= 17.0
         self.A2_dim= "Mill. EUR"
         self.A3= 17972.3152
         self.A3_dim= "Mill. EUR"
         self.A4= 48209.0
         self.A4_dim= "Mill. EUR"
         self.A5= 163553.0
         self.A5_dim= "Mill. EUR"
         self.A6= 0.3728
         self.A6_dim= "%"
         self.A7= 0.4404
         self.A7_dim= "%"
         self.A8= 0.440416
         self.A8_dim= "%"
         self.A9= 0.1099
         self.A9_dim= "%"
         self.A10= 0.00429424203289
         self.A10_dim= "%"
         self.A11= 0.225444285624
         self.A11_dim= "%"
         self.A12= 0.0
         self.A12_dim= "%"
         self.B1= 0.3728
         self.B1_dim= "%"
         self.B2= 0.0
         self.B2_dim= "Basis Points Change"
         self.B3= 0.3728
         self.B3_dim= "%"
         self.B4= -351.529319608
         self.B4_dim= "Basis Points Change"
         self.B5= 0.337647068039
         self.B5_dim= "%"
         self.B6= -581.269380059
         self.B6_dim= "Basis Points Change"
         self.B7= 0.314673061994
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 37.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#DE-SEB-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'DESEB', '', u'SEB AG', '', '', '', '', '', '', '']


class entityDESEB(CAResult):
     def __init__(self):
         self.shortname = "DESEB"
         self.origin = "DE-SEB-CA-DISCLOSURE.xls"
         self.country = "DE"
         self.bank_specific_notes = "-"
         self.A1= 31754.0
         self.A1_dim= "Mill. EUR"
         self.A2= 20.0
         self.A2_dim= "Mill. EUR"
         self.A3= 2009.0
         self.A3_dim= "Mill. EUR"
         self.A4= 11726.0
         self.A4_dim= "Mill. EUR"
         self.A5= 39721.0
         self.A5_dim= "Mill. EUR"
         self.A6= 0.171328671329
         self.A6_dim= "%"
         self.A7= 0.1357
         self.A7_dim= "%"
         self.A8= 0.135678
         self.A8_dim= "%"
         self.A9= 0.0506
         self.A9_dim= "%"
         self.A10= 0.0072
         self.A10_dim= "%"
         self.A11= 0.5629
         self.A11_dim= "%"
         self.A12= 0.0
         self.A12_dim= "%"
         self.B1= 0.171328671329
         self.B1_dim= "%"
         self.B2= -21.41
         self.B2_dim= "Basis Points Change"
         self.B3= 0.169187671329
         self.B3_dim= "%"
         self.B4= 4.52413945074
         self.B4_dim= "Basis Points Change"
         self.B5= 0.169640085274
         self.B5_dim= "%"
         self.B6= -414.012340563
         self.B6_dim= "Basis Points Change"
         self.B7= 0.127786437272
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#DE-VWFS-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'DEVWFS', '', u'Volkswagen Financial Services AG', '', '', '', '', '', '', '']


class entityDEVWFS(CAResult):
     def __init__(self):
         self.shortname = "DEVWFS"
         self.origin = "DE-VWFS-CA-DISCLOSURE.xls"
         self.country = "DE"
         self.bank_specific_notes = "Starting CET1 ratio displayed for year-end 2013 under 01.01.2014 regulations. May not exactly match EBA transparency template."
         self.A1= 98024.0
         self.A1_dim= "Mill. EUR"
         self.A2= 1312.0
         self.A2_dim= "Mill. EUR"
         self.A3= 7980.997714
         self.A3_dim= "Mill. EUR"
         self.A4= 84022.0
         self.A4_dim= "Mill. EUR"
         self.A5= 93627.0
         self.A5_dim= "Mill. EUR"
         self.A6= 0.094987
         self.A6_dim= "%"
         self.A7= 0.086432
         self.A7_dim= "%"
         self.A8= 0.095566
         self.A8_dim= "%"
         self.A9= 0.085
         self.A9_dim= "%"
         self.A10= 0.030135686
         self.A10_dim= "%"
         self.A11= 0.572359795575
         self.A11_dim= "%"
         self.A12= 0.0
         self.A12_dim= "%"
         self.B1= 0.094987
         self.B1_dim= "%"
         self.B2= -19.71
         self.B2_dim= "Basis Points Change"
         self.B3= 0.093016
         self.B3_dim= "%"
         self.B4= 47.795184867
         self.B4_dim= "Basis Points Change"
         self.B5= 0.0977955184867
         self.B5_dim= "%"
         self.B6= -234.32300887
         self.B6_dim= "Basis Points Change"
         self.B7= 0.069583699113
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 2255.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#DE-WGZ-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'DEWGZ', '', u'WGZ Bank AG Westdeutsche Genossenschafts-Zentralbank', '', '', '', '', '', '', '']


class entityDEWGZ(CAResult):
     def __init__(self):
         self.shortname = "DEWGZ"
         self.origin = "DE-WGZ-CA-DISCLOSURE.xls"
         self.country = "DE"
         self.bank_specific_notes = "Starting CET1 ratio displayed for year-end 2013 under 01.01.2014 regulations. May not exactly match EBA transparency template."
         self.A1= 90925.7
         self.A1_dim= "Mill. EUR"
         self.A2= 227.2
         self.A2_dim= "Mill. EUR"
         self.A3= 2346.12
         self.A3_dim= "Mill. EUR"
         self.A4= 22094.0
         self.A4_dim= "Mill. EUR"
         self.A5= 95508.9
         self.A5_dim= "Mill. EUR"
         self.A6= 0.106188105368
         self.A6_dim= "%"
         self.A7= 0.122353
         self.A7_dim= "%"
         self.A8= 0.122353
         self.A8_dim= "%"
         self.A9= 0.0211
         self.A9_dim= "%"
         self.A10= 0.0043
         self.A10_dim= "%"
         self.A11= 0.6011
         self.A11_dim= "%"
         self.A12= 0.00732026258803
         self.A12_dim= "%"
         self.B1= 0.106188105368
         self.B1_dim= "%"
         self.B2= -62.37
         self.B2_dim= "Basis Points Change"
         self.B3= 0.099951105368
         self.B3_dim= "%"
         self.B4= -28.8258729179
         self.B4_dim= "Basis Points Change"
         self.B5= 0.0970685180762
         self.B5_dim= "%"
         self.B6= -273.930739168
         self.B6_dim= "Basis Points Change"
         self.B7= 0.0725580314512
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 327.146
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#DE-WWB-CA_DISCLOSURE.xls
#

#DE-WWP-CA_DISCLOSURE.xls
#

#diff.xls
#

#EE-DP-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'EEDP', '', u'AS DNB Pank', '', '', '', '', '', '', '']


class entityEEDP(CAResult):
     def __init__(self):
         self.shortname = "EEDP"
         self.origin = "EE-DP-CA-DISCLOSURE.xls"
         self.country = "EE"
         self.bank_specific_notes = "-"
         self.A1= 567.0
         self.A1_dim= "Mill. EUR"
         self.A2= 4.0
         self.A2_dim= "Mill. EUR"
         self.A3= 96.599723
         self.A3_dim= "Mill. EUR"
         self.A4= 482.492
         self.A4_dim= "Mill. EUR"
         self.A5= 566.0
         self.A5_dim= "Mill. EUR"
         self.A6= 0.200209999337
         self.A6_dim= "%"
         self.A7= 0.1901
         self.A7_dim= "%"
         self.A8= 0.190056
         self.A8_dim= "%"
         self.A9= 0.16
         self.A9_dim= "%"
         self.A10= 0.0719095019974
         self.A10_dim= "%"
         self.A11= 0.361153765396
         self.A11_dim= "%"
         self.A12= 0.0
         self.A12_dim= "%"
         self.B1= 0.200209999337
         self.B1_dim= "%"
         self.B2= -580.13
         self.B2_dim= "Basis Points Change"
         self.B3= 0.142196999337
         self.B3_dim= "%"
         self.B4= -4.09544970426
         self.B4_dim= "Basis Points Change"
         self.B5= 0.141787454366
         self.B5_dim= "%"
         self.B6= -239.282193699
         self.B6_dim= "Basis Points Change"
         self.B7= 0.118268779967
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#EE-SB-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'EESB', '', u'Swedbank AS', '', '', '', '', '', '', '']


class entityEESB(CAResult):
     def __init__(self):
         self.shortname = "EESB"
         self.origin = "EE-SB-CA-DISCLOSURE.xls"
         self.country = "EE"
         self.bank_specific_notes = "-"
         self.A1= 8589.0
         self.A1_dim= "Mill. EUR"
         self.A2= 324.0
         self.A2_dim= "Mill. EUR"
         self.A3= 1724.166339
         self.A3_dim= "Mill. EUR"
         self.A4= 5296.978
         self.A4_dim= "Mill. EUR"
         self.A5= 9702.0
         self.A5_dim= "Mill. EUR"
         self.A6= 0.3255
         self.A6_dim= "%"
         self.A7= 0.3251
         self.A7_dim= "%"
         self.A8= 0.3255
         self.A8_dim= "%"
         self.A9= 0.187177901464
         self.A9_dim= "%"
         self.A10= 0.0172403681988
         self.A10_dim= "%"
         self.A11= 0.238178633975
         self.A11_dim= "%"
         self.A12= 0.0
         self.A12_dim= "%"
         self.B1= 0.3255
         self.B1_dim= "%"
         self.B2= -69.99
         self.B2_dim= "Basis Points Change"
         self.B3= 0.318501
         self.B3_dim= "%"
         self.B4= 104.82276975
         self.B4_dim= "Basis Points Change"
         self.B5= 0.328983276975
         self.B5_dim= "%"
         self.B6= 109.747009378
         self.B6_dim= "Basis Points Change"
         self.B7= 0.329475700938
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#EE-SEB-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'EESEB', '', u'AS SEB Pank', '', '', '', '', '', '', '']


class entityEESEB(CAResult):
     def __init__(self):
         self.shortname = "EESEB"
         self.origin = "EE-SEB-CA-DISCLOSURE.xls"
         self.country = "EE"
         self.bank_specific_notes = "-"
         self.A1= 4442.9
         self.A1_dim= "Mill. EUR"
         self.A2= 72.8
         self.A2_dim= "Mill. EUR"
         self.A3= 770.2596
         self.A3_dim= "Mill. EUR"
         self.A4= 3303.0
         self.A4_dim= "Mill. EUR"
         self.A5= 5503.2
         self.A5_dim= "Mill. EUR"
         self.A6= 0.2332
         self.A6_dim= "%"
         self.A7= 0.2344
         self.A7_dim= "%"
         self.A8= 0.234392
         self.A8_dim= "%"
         self.A9= 0.14
         self.A9_dim= "%"
         self.A10= 0.022
         self.A10_dim= "%"
         self.A11= 0.4769
         self.A11_dim= "%"
         self.A12= 1.7442886403e-05
         self.A12_dim= "%"
         self.B1= 0.2332
         self.B1_dim= "%"
         self.B2= -60.52
         self.B2_dim= "Basis Points Change"
         self.B3= 0.227148
         self.B3_dim= "%"
         self.B4= 90.4554620886
         self.B4_dim= "Basis Points Change"
         self.B5= 0.236193546209
         self.B5_dim= "%"
         self.B6= 62.0867785986
         self.B6_dim= "Basis Points Change"
         self.B7= 0.23335667786
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#ES-BANK-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'ESBANK', '', u'Banco Financiero y de Ahorros, S.A.', '', '', '', '', '', '', '']


class entityESBANK(CAResult):
     def __init__(self):
         self.shortname = "ESBANK"
         self.origin = "ES-BANK-CA-DISCLOSURE.xls"
         self.country = "ES"
         self.bank_specific_notes = "-"
         self.A1= 266491.0
         self.A1_dim= "Mill. EUR"
         self.A2= 2170.57
         self.A2_dim= "Mill. EUR"
         self.A3= 11253.191087
         self.A3_dim= "Mill. EUR"
         self.A4= 105344.981875
         self.A4_dim= "Mill. EUR"
         self.A5= 266644.0
         self.A5_dim= "Mill. EUR"
         self.A6= 0.106822279398
         self.A6_dim= "%"
         self.A7= 0.1182
         self.A7_dim= "%"
         self.A8= 0.118238
         self.A8_dim= "%"
         self.A9= 0.0422
         self.A9_dim= "%"
         self.A10= 0.0799599011191
         self.A10_dim= "%"
         self.A11= 0.489864123723
         self.A11_dim= "%"
         self.A12= 0.000712864599555
         self.A12_dim= "%"
         self.B1= 0.106822279398
         self.B1_dim= "%"
         self.B2= -8.09
         self.B2_dim= "Basis Points Change"
         self.B3= 0.106013279398
         self.B3_dim= "%"
         self.B4= 172.600617351
         self.B4_dim= "Basis Points Change"
         self.B5= 0.123273341133
         self.B5_dim= "%"
         self.B6= -30.4671242073
         self.B6_dim= "Basis Points Change"
         self.B7= 0.102966566977
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 1158.0
         self.C2= -166.8
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#ES-BBVA-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'ESBBVA', '', u'Banco Bilbao Vizcaya Argentaria, S.A.', '', '', '', '', '', '', '']


class entityESBBVA(CAResult):
     def __init__(self):
         self.shortname = "ESBBVA"
         self.origin = "ES-BBVA-CA-DISCLOSURE.xls"
         self.country = "ES"
         self.bank_specific_notes = "-"
         self.A1= 587084.985
         self.A1_dim= "Mill. EUR"
         self.A2= 2197.0
         self.A2_dim= "Mill. EUR"
         self.A3= 37058.304652
         self.A3_dim= "Mill. EUR"
         self.A4= 344740.946916
         self.A4_dim= "Mill. EUR"
         self.A5= 621977.660755
         self.A5_dim= "Mill. EUR"
         self.A6= 0.107496092308
         self.A6_dim= "%"
         self.A7= 0.110647
         self.A7_dim= "%"
         self.A8= 0.110647
         self.A8_dim= "%"
         self.A9= 0.0613344473043
         self.A9_dim= "%"
         self.A10= 0.0404886982517
         self.A10_dim= "%"
         self.A11= 0.655688716402
         self.A11_dim= "%"
         self.A12= 0.00143250129281
         self.A12_dim= "%"
         self.B1= 0.107496092308
         self.B1_dim= "%"
         self.B2= -20.51
         self.B2_dim= "Basis Points Change"
         self.B3= 0.105445092308
         self.B3_dim= "%"
         self.B4= -30.5071447249
         self.B4_dim= "Basis Points Change"
         self.B5= 0.102394377835
         self.B5_dim= "%"
         self.B6= -157.710999091
         self.B6_dim= "Basis Points Change"
         self.B7= 0.0896739923988
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#ES-BKT-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'ESBKT', '', u'Bankinter, S.A.', '', '', '', '', '', '', '']


class entityESBKT(CAResult):
     def __init__(self):
         self.shortname = "ESBKT"
         self.origin = "ES-BKT-CA-DISCLOSURE.xls"
         self.country = "ES"
         self.bank_specific_notes = "-"
         self.A1= 54428.9312751
         self.A1_dim= "Mill. EUR"
         self.A2= 215.188918473
         self.A2_dim= "Mill. EUR"
         self.A3= 2864.494716
         self.A3_dim= "Mill. EUR"
         self.A4= 23798.926947
         self.A4_dim= "Mill. EUR"
         self.A5= 48850.7804616
         self.A5_dim= "Mill. EUR"
         self.A6= 0.120362347528
         self.A6_dim= "%"
         self.A7= 0.1291
         self.A7_dim= "%"
         self.A8= 0.125863
         self.A8_dim= "%"
         self.A9= 0.0586356845525
         self.A9_dim= "%"
         self.A10= 0.0433581961936
         self.A10_dim= "%"
         self.A11= 0.399598385885
         self.A11_dim= "%"
         self.A12= 0.0
         self.A12_dim= "%"
         self.B1= 0.120362347528
         self.B1_dim= "%"
         self.B2= -36.61
         self.B2_dim= "Basis Points Change"
         self.B3= 0.116701347528
         self.B3_dim= "%"
         self.B4= -4.35775127108
         self.B4_dim= "Basis Points Change"
         self.B5= 0.116265572401
         self.B5_dim= "%"
         self.B6= -87.1366961223
         self.B6_dim= "Basis Points Change"
         self.B7= 0.107987677916
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 12.7
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= -4.2

#ES-BMN-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'ESBMN', '', u'Banco Mare Nostrum, S.A.', '', '', '', '', '', '', '']


class entityESBMN(CAResult):
     def __init__(self):
         self.shortname = "ESBMN"
         self.origin = "ES-BMN-CA-DISCLOSURE.xls"
         self.country = "ES"
         self.bank_specific_notes = "-"
         self.A1= 47574.0
         self.A1_dim= "Mill. EUR"
         self.A2= 22.0
         self.A2_dim= "Mill. EUR"
         self.A3= 2018.02908
         self.A3_dim= "Mill. EUR"
         self.A4= 21381.935
         self.A4_dim= "Mill. EUR"
         self.A5= 45231.0
         self.A5_dim= "Mill. EUR"
         self.A6= 0.0943800960951
         self.A6_dim= "%"
         self.A7= 0.1035
         self.A7_dim= "%"
         self.A8= 0.103487
         self.A8_dim= "%"
         self.A9= 0.0428
         self.A9_dim= "%"
         self.A10= 0.0729800976553
         self.A10_dim= "%"
         self.A11= 0.391611623318
         self.A11_dim= "%"
         self.A12= 0.00727288014462
         self.A12_dim= "%"
         self.B1= 0.0943800960951
         self.B1_dim= "%"
         self.B2= -42.61
         self.B2_dim= "Basis Points Change"
         self.B3= 0.0901190960951
         self.B3_dim= "%"
         self.B4= 128.387090072
         self.B4_dim= "Basis Points Change"
         self.B5= 0.102957805102
         self.B5_dim= "%"
         self.B6= -92.6619689603
         self.B6_dim= "Basis Points Change"
         self.B7= 0.0808528991991
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= -0.901

#ES-BSAB-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'ESBSAB', '', u'Banco de Sabadell, S.A.', '', '', '', '', '', '', '']


class entityESBSAB(CAResult):
     def __init__(self):
         self.shortname = "ESBSAB"
         self.origin = "ES-BSAB-CA-DISCLOSURE.xls"
         self.country = "ES"
         self.bank_specific_notes = "-"
         self.A1= 161544.192
         self.A1_dim= "Mill. EUR"
         self.A2= 247.832
         self.A2_dim= "Mill. EUR"
         self.A3= 8227.499
         self.A3_dim= "Mill. EUR"
         self.A4= 80189.0
         self.A4_dim= "Mill. EUR"
         self.A5= 169775.325937
         self.A5_dim= "Mill. EUR"
         self.A6= 0.10260134183
         self.A6_dim= "%"
         self.A7= 0.1201
         self.A7_dim= "%"
         self.A8= 0.11877
         self.A8_dim= "%"
         self.A9= 0.0525863382671
         self.A9_dim= "%"
         self.A10= 0.116870304979
         self.A10_dim= "%"
         self.A11= 0.520552786276
         self.A11_dim= "%"
         self.A12= 0.00498997822218
         self.A12_dim= "%"
         self.B1= 0.10260134183
         self.B1_dim= "%"
         self.B2= 0.0
         self.B2_dim= "Basis Points Change"
         self.B3= 0.10260134183
         self.B3_dim= "%"
         self.B4= -9.81229590146
         self.B4_dim= "Basis Points Change"
         self.B5= 0.10162011224
         self.B5_dim= "%"
         self.B6= -192.533420294
         self.B6_dim= "Basis Points Change"
         self.B7= 0.0833479998005
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 6.41441136
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#ES-CAJAM-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'ESCAJAM', '', u'Cajas Rurales Unidas, Sociedad Cooperativa de Cr\xe9dito', '', '', '', '', '', '', '']


class entityESCAJAM(CAResult):
     def __init__(self):
         self.shortname = "ESCAJAM"
         self.origin = "ES-CAJAM-CA-DISCLOSURE.xls"
         self.country = "ES"
         self.bank_specific_notes = "-"
         self.A1= 42096.1
         self.A1_dim= "Mill. EUR"
         self.A2= 82.881
         self.A2_dim= "Mill. EUR"
         self.A3= 2422.019683
         self.A3_dim= "Mill. EUR"
         self.A4= 22023.000325
         self.A4_dim= "Mill. EUR"
         self.A5= 42648.4225342
         self.A5_dim= "Mill. EUR"
         self.A6= 0.109976826375
         self.A6_dim= "%"
         self.A7= 0.1085
         self.A7_dim= "%"
         self.A8= 0.108467
         self.A8_dim= "%"
         self.A9= 0.0567903697074
         self.A9_dim= "%"
         self.A10= 0.148704152969
         self.A10_dim= "%"
         self.A11= 0.433353672588
         self.A11_dim= "%"
         self.A12= 0.00559253707588
         self.A12_dim= "%"
         self.B1= 0.109976826375
         self.B1_dim= "%"
         self.B2= -104.91
         self.B2_dim= "Basis Points Change"
         self.B3= 0.099485826375
         self.B3_dim= "%"
         self.B4= 22.3567158481
         self.B4_dim= "Basis Points Change"
         self.B5= 0.10172149796
         self.B5_dim= "%"
         self.B6= -196.051254938
         self.B6_dim= "Basis Points Change"
         self.B7= 0.0798807008813
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 49.73
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#ES-CX-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'ESCX', '', u'Catalunya Banc, S.A.', '', '', '', '', '', '', '']


class entityESCX(CAResult):
     def __init__(self):
         self.shortname = "ESCX"
         self.origin = "ES-CX-CA-DISCLOSURE.xls"
         self.country = "ES"
         self.bank_specific_notes = "-"
         self.A1= 63263.974
         self.A1_dim= "Mill. EUR"
         self.A2= 532.185
         self.A2_dim= "Mill. EUR"
         self.A3= 2619.1868
         self.A3_dim= "Mill. EUR"
         self.A4= 21266.126
         self.A4_dim= "Mill. EUR"
         self.A5= 67921.538
         self.A5_dim= "Mill. EUR"
         self.A6= 0.1231623851
         self.A6_dim= "%"
         self.A7= 0.1434
         self.A7_dim= "%"
         self.A8= 0.143402
         self.A8_dim= "%"
         self.A9= 0.0386
         self.A9_dim= "%"
         self.A10= 0.108357155891
         self.A10_dim= "%"
         self.A11= 0.578866124053
         self.A11_dim= "%"
         self.A12= 0.0180197342646
         self.A12_dim= "%"
         self.B1= 0.1231623851
         self.B1_dim= "%"
         self.B2= -10.27
         self.B2_dim= "Basis Points Change"
         self.B3= 0.1221353851
         self.B3_dim= "%"
         self.B4= -45.0872567489
         self.B4_dim= "Basis Points Change"
         self.B5= 0.117626659425
         self.B5_dim= "%"
         self.B6= -419.790601415
         self.B6_dim= "Basis Points Change"
         self.B7= 0.0801563249586
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= -0.5

#ES-IBER-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'ESIBER', '', u'Caja de Ahorros y M.P. de Zaragoza, Arag\xf3n y Rioja', '', '', '', '', '', '', '']


class entityESIBER(CAResult):
     def __init__(self):
         self.shortname = "ESIBER"
         self.origin = "ES-IBER-CA-DISCLOSURE.xls"
         self.country = "ES"
         self.bank_specific_notes = "For this institution, the combined impact of the Asset Quality Review and the Join Up calculation is less than 10 basis points of RWA in the most extreme scenario year. This minor impact is displayed in this template, however the accompanying transparency template reflects the Stress Test data without taking this minor impact into account. Therefore, a small difference in CET1% end point between the two disclosure materials is to be expected. This template contains the official result."
         self.A1= 58705.0
         self.A1_dim= "Mill. EUR"
         self.A2= -25.0
         self.A2_dim= "Mill. EUR"
         self.A3= 2654.992202
         self.A3_dim= "Mill. EUR"
         self.A4= 26475.376005
         self.A4_dim= "Mill. EUR"
         self.A5= 55657.0
         self.A5_dim= "Mill. EUR"
         self.A6= 0.100281567351
         self.A6_dim= "%"
         self.A7= 0.103011
         self.A7_dim= "%"
         self.A8= 0.10279
         self.A8_dim= "%"
         self.A9= 0.0479
         self.A9_dim= "%"
         self.A10= 0.0792174767129
         self.A10_dim= "%"
         self.A11= 0.585130543746
         self.A11_dim= "%"
         self.A12= 0.0
         self.A12_dim= "%"
         self.B1= 0.100281567351
         self.B1_dim= "%"
         self.B2= -1.93
         self.B2_dim= "Basis Points Change"
         self.B3= 0.100088567351
         self.B3_dim= "%"
         self.B4= 29.774653556
         self.B4_dim= "Basis Points Change"
         self.B5= 0.103066032707
         self.B5_dim= "%"
         self.B6= -219.373741094
         self.B6_dim= "Basis Points Change"
         self.B7= 0.078151193242
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#ES-KTXB-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'ESKTXB', '', u'Kutxabank, S.A.', '', '', '', '', '', '', '']


class entityESKTXB(CAResult):
     def __init__(self):
         self.shortname = "ESKTXB"
         self.origin = "ES-KTXB-CA-DISCLOSURE.xls"
         self.country = "ES"
         self.bank_specific_notes = "-"
         self.A1= 60094.818
         self.A1_dim= "Mill. EUR"
         self.A2= 108.319
         self.A2_dim= "Mill. EUR"
         self.A3= 4365.832
         self.A3_dim= "Mill. EUR"
         self.A4= 36027.387
         self.A4_dim= "Mill. EUR"
         self.A5= 61528.238
         self.A5_dim= "Mill. EUR"
         self.A6= 0.121180922724
         self.A6_dim= "%"
         self.A7= 0.1197
         self.A7_dim= "%"
         self.A8= 0.119696
         self.A8_dim= "%"
         self.A9= 0.0709590746562
         self.A9_dim= "%"
         self.A10= 0.101331739538
         self.A10_dim= "%"
         self.A11= 0.450325095171
         self.A11_dim= "%"
         self.A12= 0.00567769420651
         self.A12_dim= "%"
         self.B1= 0.121180922724
         self.B1_dim= "%"
         self.B2= -8.46
         self.B2_dim= "Basis Points Change"
         self.B3= 0.120334922724
         self.B3_dim= "%"
         self.B4= 33.1007486303
         self.B4_dim= "Basis Points Change"
         self.B5= 0.123644997587
         self.B5_dim= "%"
         self.B6= -21.5040237192
         self.B6_dim= "Basis Points Change"
         self.B7= 0.118184520352
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#ES-KXA-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'ESKXA', '', u'Caja de Ahorros y Pensiones de Barcelona', '', '', '', '', '', '', '']


class entityESKXA(CAResult):
     def __init__(self):
         self.shortname = "ESKXA"
         self.origin = "ES-KXA-CA-DISCLOSURE.xls"
         self.country = "ES"
         self.bank_specific_notes = "For this institution, the combined impact of the Asset Quality Review and the Join Up calculation is less than 10 basis points of RWA in the most extreme scenario year. This minor impact is displayed in this template, however the accompanying transparency template reflects the Stress Test data without taking this minor impact into account. Therefore, a small difference in CET1% end point between the two disclosure materials is to be expected. This template contains the official result."
         self.A1= 335127.0
         self.A1_dim= "Mill. EUR"
         self.A2= 902.0
         self.A2_dim= "Mill. EUR"
         self.A3= 17544.106444
         self.A3_dim= "Mill. EUR"
         self.A4= 170679.370666
         self.A4_dim= "Mill. EUR"
         self.A5= 339253.0
         self.A5_dim= "Mill. EUR"
         self.A6= 0.102789847276
         self.A6_dim= "%"
         self.A7= 0.127546
         self.A7_dim= "%"
         self.A8= 0.113981
         self.A8_dim= "%"
         self.A9= 0.0558701325619
         self.A9_dim= "%"
         self.A10= 0.0908
         self.A10_dim= "%"
         self.A11= 0.6194
         self.A11_dim= "%"
         self.A12= 0.0018
         self.A12_dim= "%"
         self.B1= 0.102789847276
         self.B1_dim= "%"
         self.B2= -3.56
         self.B2_dim= "Basis Points Change"
         self.B3= 0.102433847276
         self.B3_dim= "%"
         self.B4= 54.9501041271
         self.B4_dim= "Basis Points Change"
         self.B5= 0.107928857689
         self.B5_dim= "%"
         self.B6= -99.0928176816
         self.B6_dim= "Basis Points Change"
         self.B7= 0.0925245655083
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 1923.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#ES-LIBER-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'ESLIBER', '', u'Liberbank, S.A.', '', '', '', '', '', '', '']


class entityESLIBER(CAResult):
     def __init__(self):
         self.shortname = "ESLIBER"
         self.origin = "ES-LIBER-CA-DISCLOSURE.xls"
         self.country = "ES"
         self.bank_specific_notes = "-"
         self.A1= 44514.497
         self.A1_dim= "Mill. EUR"
         self.A2= 50.925
         self.A2_dim= "Mill. EUR"
         self.A3= 1565.152741
         self.A3_dim= "Mill. EUR"
         self.A4= 18080.152561
         self.A4_dim= "Mill. EUR"
         self.A5= 45435.227
         self.A5_dim= "Mill. EUR"
         self.A6= 0.0865674521119
         self.A6_dim= "%"
         self.A7= 0.103911
         self.A7_dim= "%"
         self.A8= 0.103911
         self.A8_dim= "%"
         self.A9= 0.0385
         self.A9_dim= "%"
         self.A10= 0.1064
         self.A10_dim= "%"
         self.A11= 0.4211
         self.A11_dim= "%"
         self.A12= 0.0
         self.A12_dim= "%"
         self.B1= 0.0865674521119
         self.B1_dim= "%"
         self.B2= -83.44
         self.B2_dim= "Basis Points Change"
         self.B3= 0.0782234521119
         self.B3_dim= "%"
         self.B4= 69.1154486786
         self.B4_dim= "Basis Points Change"
         self.B5= 0.0851349969798
         self.B5_dim= "%"
         self.B6= -220.250125959
         self.B6_dim= "Basis Points Change"
         self.B7= 0.056198439516
         self.B7_dim= "%"
         self.B8= 17.77
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 17.77
         self.C1= 574.843
         self.C2= 0.0
         self.C3= 61.857
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= -20.93

#ES-NCG-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'ESNCG', '', u'NCG Banco, S.A.', '', '', '', '', '', '', '']


class entityESNCG(CAResult):
     def __init__(self):
         self.shortname = "ESNCG"
         self.origin = "ES-NCG-CA-DISCLOSURE.xls"
         self.country = "ES"
         self.bank_specific_notes = "-"
         self.A1= 52591.408
         self.A1_dim= "Mill. EUR"
         self.A2= 17.9
         self.A2_dim= "Mill. EUR"
         self.A3= 2659.956645
         self.A3_dim= "Mill. EUR"
         self.A4= 25943.264008
         self.A4_dim= "Mill. EUR"
         self.A5= 50936.1180439
         self.A5_dim= "Mill. EUR"
         self.A6= 0.102529760487
         self.A6_dim= "%"
         self.A7= 0.113
         self.A7_dim= "%"
         self.A8= 0.113022
         self.A8_dim= "%"
         self.A9= 0.0521408011053
         self.A9_dim= "%"
         self.A10= 0.104532963073
         self.A10_dim= "%"
         self.A11= 0.53276412072
         self.A11_dim= "%"
         self.A12= 0.0
         self.A12_dim= "%"
         self.B1= 0.102529760487
         self.B1_dim= "%"
         self.B2= -7.22
         self.B2_dim= "Basis Points Change"
         self.B3= 0.101807760487
         self.B3_dim= "%"
         self.B4= 132.347948397
         self.B4_dim= "Basis Points Change"
         self.B5= 0.115042555327
         self.B5_dim= "%"
         self.B6= -103.699611597
         self.B6_dim= "Basis Points Change"
         self.B7= 0.0914377993277
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#ES-POPU-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'ESPOPU', '', u'Banco Popular Espa\xf1ol, S.A.', '', '', '', '', '', '', '']


class entityESPOPU(CAResult):
     def __init__(self):
         self.shortname = "ESPOPU"
         self.origin = "ES-POPU-CA-DISCLOSURE.xls"
         self.country = "ES"
         self.bank_specific_notes = "-"
         self.A1= 147079.0
         self.A1_dim= "Mill. EUR"
         self.A2= 325.0
         self.A2_dim= "Mill. EUR"
         self.A3= 8941.673641
         self.A3_dim= "Mill. EUR"
         self.A4= 84109.435862
         self.A4_dim= "Mill. EUR"
         self.A5= 143954.0
         self.A5_dim= "Mill. EUR"
         self.A6= 0.106309994228
         self.A6_dim= "%"
         self.A7= 0.119827
         self.A7_dim= "%"
         self.A8= 0.111989
         self.A8_dim= "%"
         self.A9= 0.0658
         self.A9_dim= "%"
         self.A10= 0.1431
         self.A10_dim= "%"
         self.A11= 0.4016
         self.A11_dim= "%"
         self.A12= 0.0032
         self.A12_dim= "%"
         self.B1= 0.106309994228
         self.B1_dim= "%"
         self.B2= -56.93
         self.B2_dim= "Basis Points Change"
         self.B3= 0.100616994228
         self.B3_dim= "%"
         self.B4= 13.6255653171
         self.B4_dim= "Basis Points Change"
         self.B5= 0.10197955076
         self.B5_dim= "%"
         self.B6= -249.673453858
         self.B6_dim= "Basis Points Change"
         self.B7= 0.0756496488421
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 120.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#ES-SAN-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'ESSAN', '', u'Banco Santander, S.A.', '', '', '', '', '', '', '']


class entityESSAN(CAResult):
     def __init__(self):
         self.shortname = "ESSAN"
         self.origin = "ES-SAN-CA-DISCLOSURE.xls"
         self.country = "ES"
         self.bank_specific_notes = "-"
         self.A1= 1117159.0
         self.A1_dim= "Mill. EUR"
         self.A2= 4370.0
         self.A2_dim= "Mill. EUR"
         self.A3= 56086.348901
         self.A3_dim= "Mill. EUR"
         self.A4= 540248.383
         self.A4_dim= "Mill. EUR"
         self.A5= 1250513.0
         self.A5_dim= "Mill. EUR"
         self.A6= 0.10381585705
         self.A6_dim= "%"
         self.A7= 0.1113
         self.A7_dim= "%"
         self.A8= 0.105459
         self.A8_dim= "%"
         self.A9= 0.0448735838812
         self.A9_dim= "%"
         self.A10= 0.0423637307369
         self.A10_dim= "%"
         self.A11= 0.631911592857
         self.A11_dim= "%"
         self.A12= 0.0013
         self.A12_dim= "%"
         self.B1= 0.10381585705
         self.B1_dim= "%"
         self.B2= -3.77
         self.B2_dim= "Basis Points Change"
         self.B3= 0.10343885705
         self.B3_dim= "%"
         self.B4= 70.7729679587
         self.B4_dim= "Basis Points Change"
         self.B5= 0.110516153846
         self.B5_dim= "%"
         self.B6= -139.650177735
         self.B6_dim= "Basis Points Change"
         self.B7= 0.0894738392764
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#ES-UNICN-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'ESUNICN', '', u'Unicaja Banco, S.A.', '', '', '', '', '', '', '']


class entityESUNICN(CAResult):
     def __init__(self):
         self.shortname = "ESUNICN"
         self.origin = "ES-UNICN-CA-DISCLOSURE.xls"
         self.country = "ES"
         self.bank_specific_notes = "-"
         self.A1= 77137.0862
         self.A1_dim= "Mill. EUR"
         self.A2= -9.461
         self.A2_dim= "Mill. EUR"
         self.A3= 3693.19
         self.A3_dim= "Mill. EUR"
         self.A4= 33320.728569
         self.A4_dim= "Mill. EUR"
         self.A5= 80487.695
         self.A5_dim= "Mill. EUR"
         self.A6= 0.11083761246
         self.A6_dim= "%"
         self.A7= 0.1113
         self.A7_dim= "%"
         self.A8= 0.1113
         self.A8_dim= "%"
         self.A9= 0.047
         self.A9_dim= "%"
         self.A10= 0.0829120377951
         self.A10_dim= "%"
         self.A11= 0.518133261757
         self.A11_dim= "%"
         self.A12= 0.0
         self.A12_dim= "%"
         self.B1= 0.11083761246
         self.B1_dim= "%"
         self.B2= -20.71
         self.B2_dim= "Basis Points Change"
         self.B3= 0.10876661246
         self.B3_dim= "%"
         self.B4= 24.6705182522
         self.B4_dim= "Basis Points Change"
         self.B5= 0.111233664285
         self.B5_dim= "%"
         self.B6= -198.982704002
         self.B6_dim= "Basis Points Change"
         self.B7= 0.0888683420594
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#FI-DBK-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'FIDBK', '', u'Danske Bank Oyj', '', '', '', '', '', '', '']


class entityFIDBK(CAResult):
     def __init__(self):
         self.shortname = "FIDBK"
         self.origin = "FI-DBK-CA-DISCLOSURE.xls"
         self.country = "FI"
         self.bank_specific_notes = "-"
         self.A1= 26679.9
         self.A1_dim= "Mill. EUR"
         self.A2= 145.3
         self.A2_dim= "Mill. EUR"
         self.A3= 2319.469249
         self.A3_dim= "Mill. EUR"
         self.A4= 15210.0
         self.A4_dim= "Mill. EUR"
         self.A5= 32050.0
         self.A5_dim= "Mill. EUR"
         self.A6= 0.152496334583
         self.A6_dim= "%"
         self.A7= 0.172
         self.A7_dim= "%"
         self.A8= 0.15649
         self.A8_dim= "%"
         self.A9= 0.07914
         self.A9_dim= "%"
         self.A10= 0.01821
         self.A10_dim= "%"
         self.A11= 0.42572
         self.A11_dim= "%"
         self.A12= 0.00461
         self.A12_dim= "%"
         self.B1= 0.152496334583
         self.B1_dim= "%"
         self.B2= -30.56
         self.B2_dim= "Basis Points Change"
         self.B3= 0.149440334583
         self.B3_dim= "%"
         self.B4= 23.5432404435
         self.B4_dim= "Basis Points Change"
         self.B5= 0.151794658627
         self.B5_dim= "%"
         self.B6= -153.467586572
         self.B6_dim= "Basis Points Change"
         self.B7= 0.134093575925
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#FI-NBF-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'FINBF', '', u'Nordea Bank Finland Abp', '', '', '', '', '', '', '']


class entityFINBF(CAResult):
     def __init__(self):
         self.shortname = "FINBF"
         self.origin = "FI-NBF-CA-DISCLOSURE.xls"
         self.country = "FI"
         self.bank_specific_notes = "-"
         self.A1= 304761.0
         self.A1_dim= "Mill. EUR"
         self.A2= 827.75
         self.A2_dim= "Mill. EUR"
         self.A3= 8282.96361
         self.A3_dim= "Mill. EUR"
         self.A4= 58619.7
         self.A4_dim= "Mill. EUR"
         self.A5= 241700.323594
         self.A5_dim= "Mill. EUR"
         self.A6= 0.1413
         self.A6_dim= "%"
         self.A7= 0.15
         self.A7_dim= "%"
         self.A8= 0.150329
         self.A8_dim= "%"
         self.A9= 0.0342858337362
         self.A9_dim= "%"
         self.A10= 0.0128659329941
         self.A10_dim= "%"
         self.A11= 0.340704998592
         self.A11_dim= "%"
         self.A12= 0.00784877330105
         self.A12_dim= "%"
         self.B1= 0.1413
         self.B1_dim= "%"
         self.B2= -40.34
         self.B2_dim= "Basis Points Change"
         self.B3= 0.137266
         self.B3_dim= "%"
         self.B4= 42.0714899961
         self.B4_dim= "Basis Points Change"
         self.B5= 0.141473149
         self.B5_dim= "%"
         self.B6= -333.987983415
         self.B6_dim= "Basis Points Change"
         self.B7= 0.103867201658
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 550.0
         self.C7= 0.0

#FI-POPO-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'FIPOPO', '', u'OP-Pohjola Group', '', '', '', '', '', '', '']


class entityFIPOPO(CAResult):
     def __init__(self):
         self.shortname = "FIPOPO"
         self.origin = "FI-POPO-CA-DISCLOSURE.xls"
         self.country = "FI"
         self.bank_specific_notes = "-"
         self.A1= 88989.0
         self.A1_dim= "Mill. EUR"
         self.A2= 631.0
         self.A2_dim= "Mill. EUR"
         self.A3= 6897.21885
         self.A3_dim= "Mill. EUR"
         self.A4= 40405.5
         self.A4_dim= "Mill. EUR"
         self.A5= 106812.0
         self.A5_dim= "Mill. EUR"
         self.A6= 0.1707
         self.A6_dim= "%"
         self.A7= 0.1428
         self.A7_dim= "%"
         self.A8= 0.142765
         self.A8_dim= "%"
         self.A9= 0.0661
         self.A9_dim= "%"
         self.A10= 0.0138
         self.A10_dim= "%"
         self.A11= 0.3723
         self.A11_dim= "%"
         self.A12= 2.9e-05
         self.A12_dim= "%"
         self.B1= 0.1707
         self.B1_dim= "%"
         self.B2= -70.17
         self.B2_dim= "Basis Points Change"
         self.B3= 0.163683
         self.B3_dim= "%"
         self.B4= 80.2558241297
         self.B4_dim= "Basis Points Change"
         self.B5= 0.171708582413
         self.B5_dim= "%"
         self.B6= -439.398950148
         self.B6_dim= "Basis Points Change"
         self.B7= 0.119743104985
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 1115.0
         self.C2= -2704.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#FR-BCC-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'FRBCC', '', u'Banque Centrale de Compensation (LCH Clearnet)', '', '', '', '', '', '', '']


class entityFRBCC(CAResult):
     def __init__(self):
         self.shortname = "FRBCC"
         self.origin = "FR-BCC-CA-DISCLOSURE.xls"
         self.country = "FR"
         self.bank_specific_notes = "-"
         self.A1= 238760.5
         self.A1_dim= "Mill. EUR"
         self.A2= -0.5
         self.A2_dim= "Mill. EUR"
         self.A3= 206.2
         self.A3_dim= "Mill. EUR"
         self.A4= 341.1
         self.A4_dim= "Mill. EUR"
         self.A5= 9615.3
         self.A5_dim= "Mill. EUR"
         self.A6= 0.604514805043
         self.A6_dim= "%"
         self.A7= 0.604515
         self.A7_dim= "%"
         self.A8= 0.604515
         self.A8_dim= "%"
         self.A9= 0.0215
         self.A9_dim= "%"
         self.A10= 0.0
         self.A10_dim= "%"
         self.A11= 0.0
         self.A11_dim= "%"
         self.A12= 0.0
         self.A12_dim= "%"
         self.B1= 0.604514805043
         self.B1_dim= "%"
         self.B2= 0.0
         self.B2_dim= "Basis Points Change"
         self.B3= 0.604514805043
         self.B3_dim= "%"
         self.B4= -29.3188654354
         self.B4_dim= "Basis Points Change"
         self.B5= 0.601582918499
         self.B5_dim= "%"
         self.B6= -2133.45255057
         self.B6_dim= "Basis Points Change"
         self.B7= 0.391169549985
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= None

#FR-BNPP-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'FRBNPP', '', u'BNP Paribas', '', '', '', '', '', '', '']


class entityFRBNPP(CAResult):
     def __init__(self):
         self.shortname = "FRBNPP"
         self.origin = "FR-BNPP-CA-DISCLOSURE.xls"
         self.country = "FR"
         self.bank_specific_notes = "-"
         self.A1= 1640314.21974
         self.A1_dim= "Mill. EUR"
         self.A2= 5427.971424
         self.A2_dim= "Mill. EUR"
         self.A3= 66346.736372
         self.A3_dim= "Mill. EUR"
         self.A4= 621306.907209
         self.A4_dim= "Mill. EUR"
         self.A5= 1964685.0
         self.A5_dim= "Mill. EUR"
         self.A6= 0.106785769806
         self.A6_dim= "%"
         self.A7= 0.1285
         self.A7_dim= "%"
         self.A8= 0.1175
         self.A8_dim= "%"
         self.A9= 0.037
         self.A9_dim= "%"
         self.A10= 0.0381320534787
         self.A10_dim= "%"
         self.A11= 0.559650896323
         self.A11_dim= "%"
         self.A12= 0.0126
         self.A12_dim= "%"
         self.B1= 0.106785769806
         self.B1_dim= "%"
         self.B2= -15.02
         self.B2_dim= "Basis Points Change"
         self.B3= 0.105283769806
         self.B3_dim= "%"
         self.B4= -19.887101562
         self.B4_dim= "Basis Points Change"
         self.B5= 0.10329505965
         self.B5_dim= "%"
         self.B6= -245.833223569
         self.B6_dim= "Basis Points Change"
         self.B7= 0.0807004474489
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 50.0
         self.C2= -64.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 5750.0

#FR-BPCE-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'FRBPCE', '', u'Groupe BPCE', '', '', '', '', '', '', '']


class entityFRBPCE(CAResult):
     def __init__(self):
         self.shortname = "FRBPCE"
         self.origin = "FR-BPCE-CA-DISCLOSURE.xls"
         self.country = "FR"
         self.bank_specific_notes = "-"
         self.A1= 1065430.2
         self.A1_dim= "Mill. EUR"
         self.A2= 2669.0
         self.A2_dim= "Mill. EUR"
         self.A3= 42260.485184
         self.A3_dim= "Mill. EUR"
         self.A4= 409398.544497
         self.A4_dim= "Mill. EUR"
         self.A5= 1092459.5
         self.A5_dim= "Mill. EUR"
         self.A6= 0.103225782681
         self.A6_dim= "%"
         self.A7= 0.1282
         self.A7_dim= "%"
         self.A8= 0.1137
         self.A8_dim= "%"
         self.A9= 0.0425027574991
         self.A9_dim= "%"
         self.A10= 0.0264154693772
         self.A10_dim= "%"
         self.A11= 0.53037256229
         self.A11_dim= "%"
         self.A12= 0.0137662701883
         self.A12_dim= "%"
         self.B1= 0.103225782681
         self.B1_dim= "%"
         self.B2= -28.73
         self.B2_dim= "Basis Points Change"
         self.B3= 0.100352782681
         self.B3_dim= "%"
         self.B4= 4.43951578178
         self.B4_dim= "Basis Points Change"
         self.B5= 0.100796734259
         self.B5_dim= "%"
         self.B6= -303.794649083
         self.B6_dim= "Basis Points Change"
         self.B7= 0.0699733177723
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 1105.0740002
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#FR-BPI-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'FRBPI', '', u'BPI France (Banque Publique d\u2019Investissement)', '', '', '', '', '', '', '']


class entityFRBPI(CAResult):
     def __init__(self):
         self.shortname = "FRBPI"
         self.origin = "FR-BPI-CA-DISCLOSURE.xls"
         self.country = "FR"
         self.bank_specific_notes = "Note that the bank has additional EUR 168 MM provisioning stemming from Bpifrance state guarantee funds. This amount is not included in the coverage ratio because they do not exactly match the definition of IBNR and specific provisioning, although it does constitute a buffer against potential incurred losses."
         self.A1= 53921.650688
         self.A1_dim= "Mill. EUR"
         self.A2= 384.28242929
         self.A2_dim= "Mill. EUR"
         self.A3= 13192.984892
         self.A3_dim= "Mill. EUR"
         self.A4= 43225.800014
         self.A4_dim= "Mill. EUR"
         self.A5= 61607.7866112
         self.A5_dim= "Mill. EUR"
         self.A6= 0.305210889971
         self.A6_dim= "%"
         self.A7= 0.2912
         self.A7_dim= "%"
         self.A8= 0.291245
         self.A8_dim= "%"
         self.A9= 0.214144763446
         self.A9_dim= "%"
         self.A10= 0.054302236909
         self.A10_dim= "%"
         self.A11= 0.638411166366
         self.A11_dim= "%"
         self.A12= 0.0664501170546
         self.A12_dim= "%"
         self.B1= 0.305210889971
         self.B1_dim= "%"
         self.B2= -10.58
         self.B2_dim= "Basis Points Change"
         self.B3= 0.304152889971
         self.B3_dim= "%"
         self.B4= -27.4023754596
         self.B4_dim= "Basis Points Change"
         self.B5= 0.301412652425
         self.B5_dim= "%"
         self.B6= -94.5217172927
         self.B6_dim= "Basis Points Change"
         self.B7= 0.294700718242
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#FR-CAGR-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'FRCAGR', '', u'Groupe Cr\xe9dit Agricole', '', '', '', '', '', '', '']


class entityFRCAGR(CAResult):
     def __init__(self):
         self.shortname = "FRCAGR"
         self.origin = "FR-CAGR-CA-DISCLOSURE.xls"
         self.country = "FR"
         self.bank_specific_notes = "-"
         self.A1= 1456337.53624
         self.A1_dim= "Mill. EUR"
         self.A2= 5116.378888
         self.A2_dim= "Mill. EUR"
         self.A3= 59692.147917
         self.A3_dim= "Mill. EUR"
         self.A4= 544049.09741
         self.A4_dim= "Mill. EUR"
         self.A5= 1724732.0
         self.A5_dim= "Mill. EUR"
         self.A6= 0.109718310721
         self.A6_dim= "%"
         self.A7= 0.131
         self.A7_dim= "%"
         self.A8= 0.113
         self.A8_dim= "%"
         self.A9= 0.038
         self.A9_dim= "%"
         self.A10= 0.0240501820209
         self.A10_dim= "%"
         self.A11= 0.773612231084
         self.A11_dim= "%"
         self.A12= 0.00513547087474
         self.A12_dim= "%"
         self.B1= 0.109718310721
         self.B1_dim= "%"
         self.B2= -17.74
         self.B2_dim= "Basis Points Change"
         self.B3= 0.107944310721
         self.B3_dim= "%"
         self.B4= 27.82863192
         self.B4_dim= "Basis Points Change"
         self.B5= 0.110727173913
         self.B5_dim= "%"
         self.B6= -196.094689211
         self.B6_dim= "Basis Points Change"
         self.B7= 0.0883348417997
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 627.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 3933.0
         self.C7= 0.0

#FR-CMUT-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'FRCMUT', '', u'Groupe Cr\xe9dit Mutuel', '', '', '', '', '', '', '']


class entityFRCMUT(CAResult):
     def __init__(self):
         self.shortname = "FRCMUT"
         self.origin = "FR-CMUT-CA-DISCLOSURE.xls"
         self.country = "FR"
         self.bank_specific_notes = "-"
         self.A1= 539007.0
         self.A1_dim= "Mill. EUR"
         self.A2= 2717.0
         self.A2_dim= "Mill. EUR"
         self.A3= 32859.412418
         self.A3_dim= "Mill. EUR"
         self.A4= 236968.890185
         self.A4_dim= "Mill. EUR"
         self.A5= 702646.0
         self.A5_dim= "Mill. EUR"
         self.A6= 0.138665511715
         self.A6_dim= "%"
         self.A7= 0.1451
         self.A7_dim= "%"
         self.A8= 0.145102
         self.A8_dim= "%"
         self.A9= 0.0488
         self.A9_dim= "%"
         self.A10= 0.0308514271479
         self.A10_dim= "%"
         self.A11= 0.583287436341
         self.A11_dim= "%"
         self.A12= 0.0096492
         self.A12_dim= "%"
         self.B1= 0.138665511715
         self.B1_dim= "%"
         self.B2= -10.78
         self.B2_dim= "Basis Points Change"
         self.B3= 0.137587511715
         self.B3_dim= "%"
         self.B4= 63.872411848
         self.B4_dim= "Basis Points Change"
         self.B5= 0.1439747529
         self.B5_dim= "%"
         self.B6= -84.9440759246
         self.B6_dim= "Basis Points Change"
         self.B7= 0.129093104122
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 161.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#FR-CRH-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'FRCRH', '', u'C.R.H. - Caisse de Refinancement de l\u2019Habitat', '', '', '', '', '', '', '']


class entityFRCRH(CAResult):
     def __init__(self):
         self.shortname = "FRCRH"
         self.origin = "FR-CRH-CA-DISCLOSURE.xls"
         self.country = "FR"
         self.bank_specific_notes = "-"
         self.A1= 53133.0
         self.A1_dim= "Mill. EUR"
         self.A2= 1.0
         self.A2_dim= "Mill. EUR"
         self.A3= 314.0
         self.A3_dim= "Mill. EUR"
         self.A4= 5474.0
         self.A4_dim= "Mill. EUR"
         self.A5= 53133.0
         self.A5_dim= "Mill. EUR"
         self.A6= 0.0573620752649
         self.A6_dim= "%"
         self.A7= 0.057362
         self.A7_dim= "%"
         self.A8= 0.0574
         self.A8_dim= "%"
         self.A9= 0.0059
         self.A9_dim= "%"
         self.A10= 0.0
         self.A10_dim= "%"
         self.A11= 0.0
         self.A11_dim= "%"
         self.A12= 0.0
         self.A12_dim= "%"
         self.B1= 0.0573620752649
         self.B1_dim= "%"
         self.B2= 0.0
         self.B2_dim= "Basis Points Change"
         self.B3= 0.0573620752649
         self.B3_dim= "%"
         self.B4= -6.34895125022
         self.B4_dim= "Basis Points Change"
         self.B5= 0.0567271801399
         self.B5_dim= "%"
         self.B6= -22.4742380618
         self.B6_dim= "Basis Points Change"
         self.B7= 0.0551146514587
         self.B7_dim= "%"
         self.B8= 226.38
         self.B9= 232.72895125
         self.B10= 0.0
         self.B11= 232.72895125
         self.C1= 250.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#FR-HSBC-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'FRHSBC', '', u'HSBC France', '', '', '', '', '', '', '']


class entityFRHSBC(CAResult):
     def __init__(self):
         self.shortname = "FRHSBC"
         self.origin = "FR-HSBC-CA-DISCLOSURE.xls"
         self.country = "FR"
         self.bank_specific_notes = "-"
         self.A1= 188559.0
         self.A1_dim= "Mill. EUR"
         self.A2= 383.0
         self.A2_dim= "Mill. EUR"
         self.A3= 4115.523277
         self.A3_dim= "Mill. EUR"
         self.A4= 32012.614456
         self.A4_dim= "Mill. EUR"
         self.A5= 144306.62
         self.A5_dim= "Mill. EUR"
         self.A6= 0.128559424056
         self.A6_dim= "%"
         self.A7= 0.1369
         self.A7_dim= "%"
         self.A8= 0.136876
         self.A8_dim= "%"
         self.A9= 0.0285
         self.A9_dim= "%"
         self.A10= 0.023309185041
         self.A10_dim= "%"
         self.A11= 0.429790514958
         self.A11_dim= "%"
         self.A12= 0.00106502474027
         self.A12_dim= "%"
         self.B1= 0.128559424056
         self.B1_dim= "%"
         self.B2= -26.16
         self.B2_dim= "Basis Points Change"
         self.B3= 0.125943424056
         self.B3_dim= "%"
         self.B4= -138.464589009
         self.B4_dim= "Basis Points Change"
         self.B5= 0.112096965155
         self.B5_dim= "%"
         self.B6= -599.327852473
         self.B6_dim= "Basis Points Change"
         self.B7= 0.066010638809
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#FR-LBP-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'FRLBP', '', u'La Banque Postale', '', '', '', '', '', '', '']


class entityFRLBP(CAResult):
     def __init__(self):
         self.shortname = "FRLBP"
         self.origin = "FR-LBP-CA-DISCLOSURE.xls"
         self.country = "FR"
         self.bank_specific_notes = "For this institution, the combined impact of the Asset Quality Review and the Join Up calculation is less than 10 basis points of RWA in the most extreme scenario year. This minor impact is displayed in this template, however the accompanying transparency template reflects the Stress Test data without taking this minor impact into account. Therefore, a small difference in CET1% end point between the two disclosure materials is to be expected. This template contains the official result."
         self.A1= 199225.0
         self.A1_dim= "Mill. EUR"
         self.A2= 579.136
         self.A2_dim= "Mill. EUR"
         self.A3= 5747.8
         self.A3_dim= "Mill. EUR"
         self.A4= 57239.33498
         self.A4_dim= "Mill. EUR"
         self.A5= 212493.0
         self.A5_dim= "Mill. EUR"
         self.A6= 0.100416959806
         self.A6_dim= "%"
         self.A7= 0.114
         self.A7_dim= "%"
         self.A8= 0.114
         self.A8_dim= "%"
         self.A9= 0.0307115999115
         self.A9_dim= "%"
         self.A10= 0.00333997813766
         self.A10_dim= "%"
         self.A11= 0.470864622443
         self.A11_dim= "%"
         self.A12= 0.000635623039277
         self.A12_dim= "%"
         self.B1= 0.100416959806
         self.B1_dim= "%"
         self.B2= -2.09
         self.B2_dim= "Basis Points Change"
         self.B3= 0.100207959806
         self.B3_dim= "%"
         self.B4= 8.98333653854
         self.B4_dim= "Basis Points Change"
         self.B5= 0.10110629346
         self.B5_dim= "%"
         self.B6= -87.9067645569
         self.B6_dim= "Basis Points Change"
         self.B7= 0.0914172833502
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#FR-PSA-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'FRPSA', '', u'Banque PSA Finance', '', '', '', '', '', '', '']


class entityFRPSA(CAResult):
     def __init__(self):
         self.shortname = "FRPSA"
         self.origin = "FR-PSA-CA-DISCLOSURE.xls"
         self.country = "FR"
         self.bank_specific_notes = "For this institution, the combined impact of the Asset Quality Review and the Join Up calculation is less than 10 basis points of RWA in the most extreme scenario year. This minor impact is displayed in this template, however the accompanying transparency template reflects the Stress Test data without taking this minor impact into account. Therefore, a small difference in CET1% end point between the two disclosure materials is to be expected. This template contains the official result."
         self.A1= 25151.0
         self.A1_dim= "Mill. EUR"
         self.A2= 232.0
         self.A2_dim= "Mill. EUR"
         self.A3= 2679.748659
         self.A3_dim= "Mill. EUR"
         self.A4= 19054.0
         self.A4_dim= "Mill. EUR"
         self.A5= 25952.0
         self.A5_dim= "Mill. EUR"
         self.A6= 0.140639690301
         self.A6_dim= "%"
         self.A7= 0.1295
         self.A7_dim= "%"
         self.A8= 0.129458
         self.A8_dim= "%"
         self.A9= 0.0917
         self.A9_dim= "%"
         self.A10= 0.0332523758814
         self.A10_dim= "%"
         self.A11= 0.679529259883
         self.A11_dim= "%"
         self.A12= 0.0
         self.A12_dim= "%"
         self.B1= 0.140639690301
         self.B1_dim= "%"
         self.B2= -7.01
         self.B2_dim= "Basis Points Change"
         self.B3= 0.139938690301
         self.B3_dim= "%"
         self.B4= 16.3265768625
         self.B4_dim= "Basis Points Change"
         self.B5= 0.141571347988
         self.B5_dim= "%"
         self.B6= -130.09645206
         self.B6_dim= "Basis Points Change"
         self.B7= 0.126929045095
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#FR-RCIB-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'FRRCIB', '', u'RCI Banque', '', '', '', '', '', '', '']


class entityFRRCIB(CAResult):
     def __init__(self):
         self.shortname = "FRRCIB"
         self.origin = "FR-RCIB-CA-DISCLOSURE.xls"
         self.country = "FR"
         self.bank_specific_notes = "-"
         self.A1= 29225.0
         self.A1_dim= "Mill. EUR"
         self.A2= 506.0
         self.A2_dim= "Mill. EUR"
         self.A3= 2562.0
         self.A3_dim= "Mill. EUR"
         self.A4= 21890.11
         self.A4_dim= "Mill. EUR"
         self.A5= 31273.0
         self.A5_dim= "Mill. EUR"
         self.A6= 0.117039156039
         self.A6_dim= "%"
         self.A7= 0.1448
         self.A7_dim= "%"
         self.A8= 0.144768
         self.A8_dim= "%"
         self.A9= 0.0786
         self.A9_dim= "%"
         self.A10= 0.0304079189985
         self.A10_dim= "%"
         self.A11= 0.781914893617
         self.A11_dim= "%"
         self.A12= 0.0019503849444
         self.A12_dim= "%"
         self.B1= 0.117039156039
         self.B1_dim= "%"
         self.B2= -3.0
         self.B2_dim= "Basis Points Change"
         self.B3= 0.116739156039
         self.B3_dim= "%"
         self.B4= 29.7823743867
         self.B4_dim= "Basis Points Change"
         self.B5= 0.119717393478
         self.B5_dim= "%"
         self.B6= -259.216654
         self.B6_dim= "Basis Points Change"
         self.B7= 0.090817490639
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#FR-SFL-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'FRSFL', '', u'Soci\xe9t\xe9 de Financement Local', '', '', '', '', '', '', '']


class entityFRSFL(CAResult):
     def __init__(self):
         self.shortname = "FRSFL"
         self.origin = "FR-SFL-CA-DISCLOSURE.xls"
         self.country = "FR"
         self.bank_specific_notes = "-"
         self.A1= 83528.0
         self.A1_dim= "Mill. EUR"
         self.A2= -69.0
         self.A2_dim= "Mill. EUR"
         self.A3= 1493.83541
         self.A3_dim= "Mill. EUR"
         self.A4= 6153.198969
         self.A4_dim= "Mill. EUR"
         self.A5= 78456.0
         self.A5_dim= "Mill. EUR"
         self.A6= 0.242773786046
         self.A6_dim= "%"
         self.A7= 0.297605
         self.A7_dim= "%"
         self.A8= 0.2976
         self.A8_dim= "%"
         self.A9= 0.0192104921901
         self.A9_dim= "%"
         self.A10= 0.03
         self.A10_dim= "%"
         self.A11= 0.0354310577894
         self.A11_dim= "%"
         self.A12= 0.00409680747881
         self.A12_dim= "%"
         self.B1= 0.242773786046
         self.B1_dim= "%"
         self.B2= -96.72
         self.B2_dim= "Basis Points Change"
         self.B3= 0.233101786046
         self.B3_dim= "%"
         self.B4= 23.9569749501
         self.B4_dim= "Basis Points Change"
         self.B5= 0.235497483541
         self.B5_dim= "%"
         self.B6= -1014.27538324
         self.B6_dim= "Basis Points Change"
         self.B7= 0.131674247722
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#FR-SOCG-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'FRSOCG', '', u'Soci\xe9t\xe9 G\xe9n\xe9rale', '', '', '', '', '', '', '']


class entityFRSOCG(CAResult):
     def __init__(self):
         self.shortname = "FRSOCG"
         self.origin = "FR-SOCG-CA-DISCLOSURE.xls"
         self.country = "FR"
         self.bank_specific_notes = "-"
         self.A1= 1141578.9
         self.A1_dim= "Mill. EUR"
         self.A2= 2521.6
         self.A2_dim= "Mill. EUR"
         self.A3= 37361.965916
         self.A3_dim= "Mill. EUR"
         self.A4= 343115.339363
         self.A4_dim= "Mill. EUR"
         self.A5= 1167605.6
         self.A5_dim= "Mill. EUR"
         self.A6= 0.108890398154
         self.A6_dim= "%"
         self.A7= 0.1342
         self.A7_dim= "%"
         self.A8= 0.1127
         self.A8_dim= "%"
         self.A9= 0.0371
         self.A9_dim= "%"
         self.A10= 0.0399
         self.A10_dim= "%"
         self.A11= 0.6219
         self.A11_dim= "%"
         self.A12= 0.0051
         self.A12_dim= "%"
         self.B1= 0.108890398154
         self.B1_dim= "%"
         self.B2= -21.53
         self.B2_dim= "Basis Points Change"
         self.B3= 0.106737398154
         self.B3_dim= "%"
         self.B4= -9.7584829507
         self.B4_dim= "Basis Points Change"
         self.B5= 0.105761549859
         self.B5_dim= "%"
         self.B6= -252.674582119
         self.B6_dim= "Basis Points Change"
         self.B7= 0.0814699399421
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 186.4
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#GR-ALPH-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'GRALPH', '', u'Alpha Bank, S.A.', '', '', '', '', '', '', '']


class entityGRALPH(CAResult):
     def __init__(self):
         self.shortname = "GRALPH"
         self.origin = "GR-ALPH-CA-DISCLOSURE.xls"
         self.country = "GR"
         self.bank_specific_notes = """- Please note that the AQR shortfall is calculated before any 2014 Share Capital Increase, whereas the Stress Test shortfalls incorporate 2014 Share Capital Increase. - Please note that 1200 EUR MM (100%) of "Raising of capital instruments eligible as CET1 capital" and -940 EUR MM (100%) of "Repayment of CET1 capital, buybacks" are already reflected in the dynamic balance sheet of the Stress Test. Therefore these changes should not be added to the post-Stress Test capital position in the dynamic case, as this would constitute double-counting of capital raised."""
         self.A1= 73597.536
         self.A1_dim= "Mill. EUR"
         self.A2= 2987.81301604
         self.A2_dim= "Mill. EUR"
         self.A3= 8210.971185
         self.A3_dim= "Mill. EUR"
         self.A4= 51754.0
         self.A4_dim= "Mill. EUR"
         self.A5= 76532.772
         self.A5_dim= "Mill. EUR"
         self.A6= 0.158653846756
         self.A6_dim= "%"
         self.A7= 0.1644
         self.A7_dim= "%"
         self.A8= 0.160613
         self.A8_dim= "%"
         self.A9= 0.107256868992
         self.A9_dim= "%"
         self.A10= 0.358645905677
         self.A10_dim= "%"
         self.A11= 0.477447291214
         self.A11_dim= "%"
         self.A12= 0.00102260268591
         self.A12_dim= "%"
         self.B1= 0.158653846756
         self.B1_dim= "%"
         self.B2= -182.03
         self.B2_dim= "Basis Points Change"
         self.B3= 0.140450846756
         self.B3_dim= "%"
         self.B4= -23.8092878019
         self.B4_dim= "Basis Points Change"
         self.B5= 0.138069917976
         self.B5_dim= "%"
         self.B6= -597.595336742
         self.B6_dim= "Basis Points Change"
         self.B7= 0.0806913130816
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 1200.0
         self.C2= -940.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#GR-EURO-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'GREURO', '', u'Eurobank Ergasias, S.A.', '', '', '', '', '', '', '']


class entityGREURO(CAResult):
     def __init__(self):
         self.shortname = "GREURO"
         self.origin = "GR-EURO-CA-DISCLOSURE.xls"
         self.country = "GR"
         self.bank_specific_notes = """- Please note that the AQR shortfall is calculated before any 2014 Share Capital Increase, whereas the Stress Test shortfalls incorporate 2014 Share Capital Increase.
- Please note that 2864 EUR MM (100%) of "Raising of capital instruments eligibile as CET1 capital" is already reflected in the dynamic balance sheet of the Stress Test.  Therefore these changes should not be added to the post-Stress Test capital position in the dynamic case, as this would constitute double-counting of capital raised.
- The AQR impact and resultant CET1 % Ratio do not take into account potential mitigating measures coming from restructuring activity and/or capital increases that have taken place between January and September 2014. Conversely, dynamic stress test outcomes both in the baseline and adverse scenarios already embed the capital increases and restructuring measures that have occurred during this period of time. Therefore the shortfall (due to the AQR) displayed in line B8.A from the page: “approved restructuring results”, has been fully mitigated by the capital increase that is presented in the line C1 of the “main results and overview” worksheet.”"""
         self.A1= 76692.57
         self.A1_dim= "Mill. EUR"
         self.A2= -1153.72
         self.A2_dim= "Mill. EUR"
         self.A3= 4048.816672
         self.A3_dim= "Mill. EUR"
         self.A4= 38114.0
         self.A4_dim= "Mill. EUR"
         self.A5= 82153.69
         self.A5_dim= "Mill. EUR"
         self.A6= 0.106229119798
         self.A6_dim= "%"
         self.A7= 0.1115
         self.A7_dim= "%"
         self.A8= 0.104259
         self.A8_dim= "%"
         self.A9= 0.0493
         self.A9_dim= "%"
         self.A10= 0.321975042737
         self.A10_dim= "%"
         self.A11= 0.46275489799
         self.A11_dim= "%"
         self.A12= 0.00365953321668
         self.A12_dim= "%"
         self.B1= 0.106229119798
         self.B1_dim= "%"
         self.B2= -280.83
         self.B2_dim= "Basis Points Change"
         self.B3= 0.0781461197985
         self.B3_dim= "%"
         self.B4= -578.902027039
         self.B4_dim= "Basis Points Change"
         self.B5= 0.0202559170946
         self.B5_dim= "%"
         self.B6= -1423.42923862
         self.B6_dim= "Basis Points Change"
         self.B7= -0.0641968040635
         self.B7_dim= "%"
         self.B8= 18.54
         self.B9= 597.442027039
         self.B10= 1191.96923862
         self.B11= 1191.96923862
         self.C1= 2864.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= -6.714

#GR-NBG-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'GRNBG', '', u'National Bank of Greece, S.A.', '', '', '', '', '', '', '']


class entityGRNBG(CAResult):
     def __init__(self):
         self.shortname = "GRNBG"
         self.origin = "GR-NBG-CA-DISCLOSURE.xls"
         self.country = "GR"
         self.bank_specific_notes = """-Please note that the AQR shortfall is calculated before any 2014 Share Capital Increase, whereas the Stress Test shortfalls incorporate 2014 Share Capital Increase.
- The AQR impact and resultant CET1 % Ratio do not take into account potential mitigating measures coming from restructuring activity and/or capital increases that have taken place between January and September 2014. Conversely, dynamic stress test outcomes both in the baseline and adverse scenarios already embed the capital increases and restructuring measures that have occurred during this period of time. Therefore the shortfall (due to the AQR) displayed in line B8.A from the page: “approved restructuring results”, has been fully mitigated by the capital increase that is presented in the line C1 of the “main results and overview” worksheet.”
- Please note that 2500 EUR MM (100%) of "Raising of capital instruments eligibile as CET1 capital" is already reflected in the dynamic balance sheet of the Stress Test.  Therefore these changes should not be added to the post-Stress Test capital position in the dynamic case, as this would constitute double-counting of capital raised."""
         self.A1= 109111.0
         self.A1_dim= "Mill. EUR"
         self.A2= 807.0
         self.A2_dim= "Mill. EUR"
         self.A3= 6058.0
         self.A3_dim= "Mill. EUR"
         self.A4= 56685.0
         self.A4_dim= "Mill. EUR"
         self.A5= 107833.0
         self.A5_dim= "Mill. EUR"
         self.A6= 0.106871306342
         self.A6_dim= "%"
         self.A7= 0.1122
         self.A7_dim= "%"
         self.A8= 0.102774
         self.A8_dim= "%"
         self.A9= 0.0562
         self.A9_dim= "%"
         self.A10= 0.2903
         self.A10_dim= "%"
         self.A11= 0.3978
         self.A11_dim= "%"
         self.A12= 0.0013
         self.A12_dim= "%"
         self.B1= 0.106871306342
         self.B1_dim= "%"
         self.B2= -316.92
         self.B2_dim= "Basis Points Change"
         self.B3= 0.0751793063421
         self.B3_dim= "%"
         self.B4= -177.087941661
         self.B4_dim= "Basis Points Change"
         self.B5= 0.057470512176
         self.B5_dim= "%"
         self.B6= -794.272048142
         self.B6_dim= "Basis Points Change"
         self.B7= -0.00424789847211
         self.B7_dim= "%"
         self.B8= 48.21
         self.B9= 225.297941661
         self.B10= 592.482048142
         self.B11= 592.482048142
         self.C1= 2500.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= -18.0

#GR-PIRE-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'GRPIRE', '', u'Piraeus Bank, S.A.', '', '', '', '', '', '', '']


class entityGRPIRE(CAResult):
     def __init__(self):
         self.shortname = "GRPIRE"
         self.origin = "GR-PIRE-CA-DISCLOSURE.xls"
         self.country = "GR"
         self.bank_specific_notes = """-Please note that the AQR shortfall is calculated before any 2014 Share Capital Increase, whereas the Stress Test shortfalls incorporate 2014 Share Capital Increase.
- Please note that 1750 EUR MM (100%) of "Raising of capital instruments eligible as CET1 capital" and -750 EUR MM (100%) of "Repayment of CET1 capital, buybacks" are already reflected in the dynamic balance sheet of the Stress Test.  Therefore these changes should not be added to the post-Stress Test capital position in the dynamic case, as this would constitute double-counting of capital raised."""
         self.A1= 92010.0
         self.A1_dim= "Mill. EUR"
         self.A2= 2546.0
         self.A2_dim= "Mill. EUR"
         self.A3= 8170.747103
         self.A3_dim= "Mill. EUR"
         self.A4= 59716.0
         self.A4_dim= "Mill. EUR"
         self.A5= 95534.0
         self.A5_dim= "Mill. EUR"
         self.A6= 0.136826765071
         self.A6_dim= "%"
         self.A7= 0.1405
         self.A7_dim= "%"
         self.A8= 0.138753
         self.A8_dim= "%"
         self.A9= 0.0859
         self.A9_dim= "%"
         self.A10= 0.332608822513
         self.A10_dim= "%"
         self.A11= 0.429041330929
         self.A11_dim= "%"
         self.A12= 0.00211311813933
         self.A12_dim= "%"
         self.B1= 0.136826765071
         self.B1_dim= "%"
         self.B2= -370.35
         self.B2_dim= "Basis Points Change"
         self.B3= 0.0997917650713
         self.B3_dim= "%"
         self.B4= -94.5170447063
         self.B4_dim= "Basis Points Change"
         self.B5= 0.0903400606007
         self.B5_dim= "%"
         self.B6= -558.442462061
         self.B6_dim= "Basis Points Change"
         self.B7= 0.0439475188652
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 110.522462061
         self.B11= 110.522462061
         self.C1= 1750.0
         self.C2= -750.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#IE-AIB-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'IEAIB', '', u'Allied Irish Banks plc', '', '', '', '', '', '', '']


class entityIEAIB(CAResult):
     def __init__(self):
         self.shortname = "IEAIB"
         self.origin = "IE-AIB-CA-DISCLOSURE.xls"
         self.country = "IE"
         self.bank_specific_notes = "-"
         self.A1= 117734.351
         self.A1_dim= "Mill. EUR"
         self.A2= -1596.828
         self.A2_dim= "Mill. EUR"
         self.A3= 9123.608305
         self.A3_dim= "Mill. EUR"
         self.A4= 60883.411284
         self.A4_dim= "Mill. EUR"
         self.A5= 128432.013712
         self.A5_dim= "Mill. EUR"
         self.A6= 0.149853763325
         self.A6_dim= "%"
         self.A7= 0.143056
         self.A7_dim= "%"
         self.A8= 0.143056
         self.A8_dim= "%"
         self.A9= 0.0710384275792
         self.A9_dim= "%"
         self.A10= 0.223159614843
         self.A10_dim= "%"
         self.A11= 0.443578404851
         self.A11_dim= "%"
         self.A12= 0.00454412833176
         self.A12_dim= "%"
         self.B1= 0.149853763325
         self.B1_dim= "%"
         self.B2= -34.66
         self.B2_dim= "Basis Points Change"
         self.B3= 0.146387763325
         self.B3_dim= "%"
         self.B4= -220.723770593
         self.B4_dim= "Basis Points Change"
         self.B5= 0.124315386266
         self.B5_dim= "%"
         self.B6= -771.658418146
         self.B6_dim= "Basis Points Change"
         self.B7= 0.0692219215108
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#IE-BAML-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'IEBAML', '', u'Merrill Lynch International Bank Limited', '', '', '', '', '', '', '']


class entityIEBAML(CAResult):
     def __init__(self):
         self.shortname = "IEBAML"
         self.origin = "IE-BAML-CA-DISCLOSURE.xls"
         self.country = "IE"
         self.bank_specific_notes = "N.B: The exposures referenced in the Fair Value asset review (Section D of Detailed AQR Results) include a securitisation portfolio which is typically accounted at cost. "
         self.A1= 294675.612493
         self.A1_dim= "Mill. EUR"
         self.A2= -218.291639475
         self.A2_dim= "Mill. EUR"
         self.A3= 5988.555616
         self.A3_dim= "Mill. EUR"
         self.A4= 39487.505016
         self.A4_dim= "Mill. EUR"
         self.A5= 74028.8696976
         self.A5_dim= "Mill. EUR"
         self.A6= 0.151656976392
         self.A6_dim= "%"
         self.A7= 0.166915
         self.A7_dim= "%"
         self.A8= 0.166915
         self.A8_dim= "%"
         self.A9= 0.0870519766152
         self.A9_dim= "%"
         self.A10= 0.025767599376
         self.A10_dim= "%"
         self.A11= 0.444767004621
         self.A11_dim= "%"
         self.A12= 3.2333700547e-06
         self.A12_dim= "%"
         self.B1= 0.151656976392
         self.B1_dim= "%"
         self.B2= -27.21
         self.B2_dim= "Basis Points Change"
         self.B3= 0.148935976392
         self.B3_dim= "%"
         self.B4= -395.339312926
         self.B4_dim= "Basis Points Change"
         self.B5= 0.1094020451
         self.B5_dim= "%"
         self.B6= -542.38495057
         self.B6_dim= "Basis Points Change"
         self.B7= 0.0946974813352
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#IE-BIRE-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'IEBIRE', '', u'The Governor and Company of the Bank of Ireland', '', '', '', '', '', '', '']


class entityIEBIRE(CAResult):
     def __init__(self):
         self.shortname = "IEBIRE"
         self.origin = "IE-BIRE-CA-DISCLOSURE.xls"
         self.country = "IE"
         self.bank_specific_notes = "-"
         self.A1= 120218.0
         self.A1_dim= "Mill. EUR"
         self.A2= -490.0
         self.A2_dim= "Mill. EUR"
         self.A3= 6850.63462
         self.A3_dim= "Mill. EUR"
         self.A4= 55264.482846
         self.A4_dim= "Mill. EUR"
         self.A5= 139861.0
         self.A5_dim= "Mill. EUR"
         self.A6= 0.123960892552
         self.A6_dim= "%"
         self.A7= 0.123933
         self.A7_dim= "%"
         self.A8= 0.122294
         self.A8_dim= "%"
         self.A9= 0.0486
         self.A9_dim= "%"
         self.A10= 0.142479583176
         self.A10_dim= "%"
         self.A11= 0.482136003293
         self.A11_dim= "%"
         self.A12= 0.0044
         self.A12_dim= "%"
         self.B1= 0.123960892552
         self.B1_dim= "%"
         self.B2= -58.05
         self.B2_dim= "Basis Points Change"
         self.B3= 0.118155892552
         self.B3_dim= "%"
         self.B4= 61.6064564924
         self.B4_dim= "Basis Points Change"
         self.B5= 0.124316538201
         self.B5_dim= "%"
         self.B6= -250.292651726
         self.B6_dim= "Basis Points Change"
         self.B7= 0.0931266273791
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#IE-PTSB-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'IEPTSB', '', u'Permanent tsb plc.', '', '', '', '', '', '', '']


class entityIEPTSB(CAResult):
     def __init__(self):
         self.shortname = "IEPTSB"
         self.origin = "IE-PTSB-CA-DISCLOSURE.xls"
         self.country = "IE"
         self.bank_specific_notes = "-"
         self.A1= 37203.0
         self.A1_dim= "Mill. EUR"
         self.A2= -262.0
         self.A2_dim= "Mill. EUR"
         self.A3= 2202.745606
         self.A3_dim= "Mill. EUR"
         self.A4= 16775.225081
         self.A4_dim= "Mill. EUR"
         self.A5= 48600.35
         self.A5_dim= "Mill. EUR"
         self.A6= 0.131309451609
         self.A6_dim= "%"
         self.A7= 0.131073
         self.A7_dim= "%"
         self.A8= 0.131073
         self.A8_dim= "%"
         self.A9= 0.0502
         self.A9_dim= "%"
         self.A10= 0.178636382068
         self.A10_dim= "%"
         self.A11= 0.414279488925
         self.A11_dim= "%"
         self.A12= 0.0
         self.A12_dim= "%"
         self.B1= 0.131309451609
         self.B1_dim= "%"
         self.B2= -29.39
         self.B2_dim= "Basis Points Change"
         self.B3= 0.128370451609
         self.B3_dim= "%"
         self.B4= -402.155456184
         self.B4_dim= "Basis Points Change"
         self.B5= 0.0881549059904
         self.B5_dim= "%"
         self.B6= -1187.12135132
         self.B6_dim= "Basis Points Change"
         self.B7= 0.00965831647707
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 453.421351317
         self.B11= 453.421351317
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= -1.0

#IE-UBIL-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'IEUBIL', '', u'Ulster Bank Ireland Limited', '', '', '', '', '', '', '']


class entityIEUBIL(CAResult):
     def __init__(self):
         self.shortname = "IEUBIL"
         self.origin = "IE-UBIL-CA-DISCLOSURE.xls"
         self.country = "IE"
         self.bank_specific_notes = "For this institution, the net impact of the AQR exercise was zero. Although individual components of the AQR process did have non-zero findings e.g. (Credit File Review), the overall impact was zero."
         self.A1= 35373.0
         self.A1_dim= "Mill. EUR"
         self.A2= -4273.0
         self.A2_dim= "Mill. EUR"
         self.A3= 4491.034418
         self.A3_dim= "Mill. EUR"
         self.A4= 38878.736038
         self.A4_dim= "Mill. EUR"
         self.A5= 38656.0
         self.A5_dim= "Mill. EUR"
         self.A6= 0.115513899773
         self.A6_dim= "%"
         self.A7= 0.115367
         self.A7_dim= "%"
         self.A8= 0.115367
         self.A8_dim= "%"
         self.A9= 0.1162
         self.A9_dim= "%"
         self.A10= 0.396327853083
         self.A10_dim= "%"
         self.A11= 0.658489453583
         self.A11_dim= "%"
         self.A12= 0.000254
         self.A12_dim= "%"
         self.B1= 0.115513899773
         self.B1_dim= "%"
         self.B2= 0.0
         self.B2_dim= "Basis Points Change"
         self.B3= 0.115513899773
         self.B3_dim= "%"
         self.B4= -153.166406577
         self.B4_dim= "Basis Points Change"
         self.B5= 0.100197259115
         self.B5_dim= "%"
         self.B6= -533.913963254
         self.B6_dim= "Basis Points Change"
         self.B7= 0.0621225034478
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#IT-BAPO-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'ITBAPO', '', u'Banco Popolare - Societ\xe0 Cooperativa', '', '', '', '', '', '', '']


class entityITBAPO(CAResult):
     def __init__(self):
         self.shortname = "ITBAPO"
         self.origin = "IT-BAPO-CA-DISCLOSURE.xls"
         self.country = "IT"
         self.bank_specific_notes = "-"
         self.A1= 126459.0
         self.A1_dim= "Mill. EUR"
         self.A2= 616.0
         self.A2_dim= "Mill. EUR"
         self.A3= 5312.2836
         self.A3_dim= "Mill. EUR"
         self.A4= 52806.0
         self.A4_dim= "Mill. EUR"
         self.A5= 114799.0
         self.A5_dim= "Mill. EUR"
         self.A6= 0.1006
         self.A6_dim= "%"
         self.A7= 0.106
         self.A7_dim= "%"
         self.A8= 0.097036
         self.A8_dim= "%"
         self.A9= 0.0338
         self.A9_dim= "%"
         self.A10= 0.190021198848
         self.A10_dim= "%"
         self.A11= 0.375137828162
         self.A11_dim= "%"
         self.A12= 0.00385
         self.A12_dim= "%"
         self.B1= 0.1006
         self.B1_dim= "%"
         self.B2= -212.4
         self.B2_dim= "Basis Points Change"
         self.B3= 0.07936
         self.B3_dim= "%"
         self.B4= -123.864369005
         self.B4_dim= "Basis Points Change"
         self.B5= 0.0669735630995
         self.B5_dim= "%"
         self.B6= -320.454186801
         self.B6_dim= "Basis Points Change"
         self.B7= 0.0473145813199
         self.B7_dim= "%"
         self.B8= 6.4
         self.B9= 130.264369005
         self.B10= 76.8541868011
         self.B11= 130.264369005
         self.C1= 1755.6
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#IT-BPER-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'ITBPER', '', u"Banca Popolare Dell'Emilia Romagna - Societ\xe0 Cooperativa", '', '', '', '', '', '', '']


class entityITBPER(CAResult):
     def __init__(self):
         self.shortname = "ITBPER"
         self.origin = "IT-BPER-CA-DISCLOSURE.xls"
         self.country = "IT"
         self.bank_specific_notes = "-"
         self.A1= 61759.0
         self.A1_dim= "Mill. EUR"
         self.A2= 6.0
         self.A2_dim= "Mill. EUR"
         self.A3= 3965.976
         self.A3_dim= "Mill. EUR"
         self.A4= 43344.0
         self.A4_dim= "Mill. EUR"
         self.A5= 65319.98
         self.A5_dim= "Mill. EUR"
         self.A6= 0.0915
         self.A6_dim= "%"
         self.A7= 0.0861
         self.A7_dim= "%"
         self.A8= 0.085576
         self.A8_dim= "%"
         self.A9= 0.0610992209356
         self.A9_dim= "%"
         self.A10= 0.118770604829
         self.A10_dim= "%"
         self.A11= 0.358216061962
         self.A11_dim= "%"
         self.A12= 0.0082066383046
         self.A12_dim= "%"
         self.B1= 0.0915
         self.B1_dim= "%"
         self.B2= -77.81
         self.B2_dim= "Basis Points Change"
         self.B3= 0.083719
         self.B3_dim= "%"
         self.B4= -3.70671756398
         self.B4_dim= "Basis Points Change"
         self.B5= 0.0833483282436
         self.B5_dim= "%"
         self.B6= -315.514067831
         self.B6_dim= "Basis Points Change"
         self.B7= 0.0521675932169
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 28.3240678311
         self.B11= 28.3240678311
         self.C1= 759.135
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= -10.122

#IT-BPM-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'ITBPM', '', u'Banca Popolare Di Milano - Societ\xe0 Cooperativa A Responsabilit\xe0 Limita', '', '', '', '', '', '', '']


class entityITBPM(CAResult):
     def __init__(self):
         self.shortname = "ITBPM"
         self.origin = "IT-BPM-CA-DISCLOSURE.xls"
         self.country = "IT"
         self.bank_specific_notes = "-"
         self.A1= 49353.318
         self.A1_dim= "Mill. EUR"
         self.A2= 29.589
         self.A2_dim= "Mill. EUR"
         self.A3= 3164.7348
         self.A3_dim= "Mill. EUR"
         self.A4= 43412.0
         self.A4_dim= "Mill. EUR"
         self.A5= 53567.8571571
         self.A5_dim= "Mill. EUR"
         self.A6= 0.0729
         self.A6_dim= "%"
         self.A7= 0.0782
         self.A7_dim= "%"
         self.A8= 0.072055
         self.A8_dim= "%"
         self.A9= 0.0614630767826
         self.A9_dim= "%"
         self.A10= 0.103951903507
         self.A10_dim= "%"
         self.A11= 0.339738108967
         self.A11_dim= "%"
         self.A12= 0.017033752559
         self.A12_dim= "%"
         self.B1= 0.0729
         self.B1_dim= "%"
         self.B2= -39.92
         self.B2_dim= "Basis Points Change"
         self.B3= 0.068908
         self.B3_dim= "%"
         self.B4= -35.4937860874
         self.B4_dim= "Basis Points Change"
         self.B5= 0.0653586213913
         self.B5_dim= "%"
         self.B6= -292.567041003
         self.B6_dim= "Basis Points Change"
         self.B7= 0.0396512958997
         self.B7_dim= "%"
         self.B8= 110.92
         self.B9= 146.413786087
         self.B10= 153.487041003
         self.B11= 153.487041003
         self.C1= 518.499
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= -1.79174264

#IT-BPS-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'ITBPS', '', u'Banca Popolare di Sondrio, Societ\xe0 Cooperativa per Azioni', '', '', '', '', '', '', '']


class entityITBPS(CAResult):
     def __init__(self):
         self.shortname = "ITBPS"
         self.origin = "IT-BPS-CA-DISCLOSURE.xls"
         self.country = "IT"
         self.bank_specific_notes = "-"
         self.A1= 32769.0
         self.A1_dim= "Mill. EUR"
         self.A2= 53.0
         self.A2_dim= "Mill. EUR"
         self.A3= 1923.563
         self.A3_dim= "Mill. EUR"
         self.A4= 23602.0
         self.A4_dim= "Mill. EUR"
         self.A5= 36816.0
         self.A5_dim= "Mill. EUR"
         self.A6= 0.0815
         self.A6_dim= "%"
         self.A7= 0.078937
         self.A7_dim= "%"
         self.A8= 0.078937
         self.A8_dim= "%"
         self.A9= 0.0523
         self.A9_dim= "%"
         self.A10= 0.0992
         self.A10_dim= "%"
         self.A11= 0.3716
         self.A11_dim= "%"
         self.A12= 0.0054
         self.A12_dim= "%"
         self.B1= 0.0815
         self.B1_dim= "%"
         self.B2= -77.75
         self.B2_dim= "Basis Points Change"
         self.B3= 0.073725
         self.B3_dim= "%"
         self.B4= -13.338448529
         self.B4_dim= "Basis Points Change"
         self.B5= 0.0723911551471
         self.B5_dim= "%"
         self.B6= -317.124044504
         self.B6_dim= "Basis Points Change"
         self.B7= 0.0420125955496
         self.B7_dim= "%"
         self.B8= 62.75
         self.B9= 76.088448529
         self.B10= 129.874044504
         self.B11= 129.874044504
         self.C1= 343.268
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= -0.756

#IT-BPV-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'ITBPV', '', u'Banca Popolare di Vicenza - Societ\xe0 Cooperativa per Azioni', '', '', '', '', '', '', '']


class entityITBPV(CAResult):
     def __init__(self):
         self.shortname = "ITBPV"
         self.origin = "IT-BPV-CA-DISCLOSURE.xls"
         self.country = "IT"
         self.bank_specific_notes = "-"
         self.A1= 45234.576
         self.A1_dim= "Mill. EUR"
         self.A2= -28.228
         self.A2_dim= "Mill. EUR"
         self.A3= 2669.341929
         self.A3_dim= "Mill. EUR"
         self.A4= 28478.069
         self.A4_dim= "Mill. EUR"
         self.A5= 48754.883
         self.A5_dim= "Mill. EUR"
         self.A6= 0.093733248873
         self.A6_dim= "%"
         self.A7= 0.0921
         self.A7_dim= "%"
         self.A8= 0.092137
         self.A8_dim= "%"
         self.A9= 0.0547454986935
         self.A9_dim= "%"
         self.A10= 0.0837441615604
         self.A10_dim= "%"
         self.A11= 0.3693359789
         self.A11_dim= "%"
         self.A12= 0.00965725864215
         self.A12_dim= "%"
         self.B1= 0.093733248873
         self.B1_dim= "%"
         self.B2= -178.75
         self.B2_dim= "Basis Points Change"
         self.B3= 0.075858248873
         self.B3_dim= "%"
         self.B4= -13.0795702633
         self.B4_dim= "Basis Points Change"
         self.B5= 0.0745502918467
         self.B5_dim= "%"
         self.B6= -441.392529933
         self.B6_dim= "Basis Points Change"
         self.B7= 0.0317189958797
         self.B7_dim= "%"
         self.B8= 41.42
         self.B9= 54.4995702633
         self.B10= 232.812529933
         self.B11= 232.812529933
         self.C1= 654.3
         self.C2= -194.9
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= -6.9

#IT-CARI-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'ITCARI', '', u'Banca Carige S.P.A. - Cassa di Risparmio di Genova e Imperia', '', '', '', '', '', '', '']


class entityITCARI(CAResult):
     def __init__(self):
         self.shortname = "ITCARI"
         self.origin = "IT-CARI-CA-DISCLOSURE.xls"
         self.country = "IT"
         self.bank_specific_notes = "-"
         self.A1= 37019.522
         self.A1_dim= "Mill. EUR"
         self.A2= -1761.657
         self.A2_dim= "Mill. EUR"
         self.A3= 1188.50159
         self.A3_dim= "Mill. EUR"
         self.A4= 22988.87
         self.A4_dim= "Mill. EUR"
         self.A5= 39526.806
         self.A5_dim= "Mill. EUR"
         self.A6= 0.0516989999943
         self.A6_dim= "%"
         self.A7= 0.058348
         self.A7_dim= "%"
         self.A8= 0.050928
         self.A8_dim= "%"
         self.A9= 0.029
         self.A9_dim= "%"
         self.A10= 0.161496045464
         self.A10_dim= "%"
         self.A11= 0.353404717861
         self.A11_dim= "%"
         self.A12= 0.0
         self.A12_dim= "%"
         self.B1= 0.0516989999943
         self.B1_dim= "%"
         self.B2= -128.69
         self.B2_dim= "Basis Points Change"
         self.B3= 0.0388299999943
         self.B3_dim= "%"
         self.B4= -154.168133072
         self.B4_dim= "Basis Points Change"
         self.B5= 0.0234131866871
         self.B5_dim= "%"
         self.B6= -624.430190805
         self.B6_dim= "Basis Points Change"
         self.B7= -0.0236130190862
         self.B7_dim= "%"
         self.B8= 411.7
         self.B9= 565.868133072
         self.B10= 786.130190805
         self.B11= 786.130190805
         self.C1= 1021.174
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= -2.48512422

#IT-CRED-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'ITCRED', '', u'Credito Emiliano S.p.A.', '', '', '', '', '', '', '']


class entityITCRED(CAResult):
     def __init__(self):
         self.shortname = "ITCRED"
         self.origin = "IT-CRED-CA-DISCLOSURE.xls"
         self.country = "IT"
         self.bank_specific_notes = "-"
         self.A1= 28349.0
         self.A1_dim= "Mill. EUR"
         self.A2= 116.0
         self.A2_dim= "Mill. EUR"
         self.A3= 1768.644
         self.A3_dim= "Mill. EUR"
         self.A4= 16152.0
         self.A4_dim= "Mill. EUR"
         self.A5= 28647.0
         self.A5_dim= "Mill. EUR"
         self.A6= 0.1095
         self.A6_dim= "%"
         self.A7= 0.0994
         self.A7_dim= "%"
         self.A8= 0.099437
         self.A8_dim= "%"
         self.A9= 0.0617
         self.A9_dim= "%"
         self.A10= 0.0448
         self.A10_dim= "%"
         self.A11= 0.3837
         self.A11_dim= "%"
         self.A12= 0.0021
         self.A12_dim= "%"
         self.B1= 0.1095
         self.B1_dim= "%"
         self.B2= -8.63
         self.B2_dim= "Basis Points Change"
         self.B3= 0.108637
         self.B3_dim= "%"
         self.B4= 4.593634638
         self.B4_dim= "Basis Points Change"
         self.B5= 0.109096363464
         self.B5_dim= "%"
         self.B6= -197.654980748
         self.B6_dim= "Basis Points Change"
         self.B7= 0.0888715019252
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= -1.764

#IT-CRVA-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'ITCRVA', '', u'Banca Piccolo Credito Valtellinese, Societ\xe0 Cooperativa', '', '', '', '', '', '', '']


class entityITCRVA(CAResult):
     def __init__(self):
         self.shortname = "ITCRVA"
         self.origin = "IT-CRVA-CA-DISCLOSURE.xls"
         self.country = "IT"
         self.bank_specific_notes = "-"
         self.A1= 27203.0
         self.A1_dim= "Mill. EUR"
         self.A2= 12.0
         self.A2_dim= "Mill. EUR"
         self.A3= 1590.09552
         self.A3_dim= "Mill. EUR"
         self.A4= 18096.0
         self.A4_dim= "Mill. EUR"
         self.A5= 28651.0
         self.A5_dim= "Mill. EUR"
         self.A6= 0.08787
         self.A6_dim= "%"
         self.A7= 0.0863
         self.A7_dim= "%"
         self.A8= 0.086298
         self.A8_dim= "%"
         self.A9= 0.0557
         self.A9_dim= "%"
         self.A10= 0.155410109497
         self.A10_dim= "%"
         self.A11= 0.352912210258
         self.A11_dim= "%"
         self.A12= 0.0026
         self.A12_dim= "%"
         self.B1= 0.08787
         self.B1_dim= "%"
         self.B2= -127.07
         self.B2_dim= "Basis Points Change"
         self.B3= 0.075163
         self.B3_dim= "%"
         self.B4= -56.9853647945
         self.B4_dim= "Basis Points Change"
         self.B5= 0.0694644635206
         self.B5_dim= "%"
         self.B6= -401.119946093
         self.B6_dim= "Basis Points Change"
         self.B7= 0.0350510053907
         self.B7_dim= "%"
         self.B8= 48.37
         self.B9= 105.355364794
         self.B10= 199.489946093
         self.B11= 199.489946093
         self.C1= 415.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#IT-ICCH-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'ITICCH', '', u'Iccrea Holding S.p.A', '', '', '', '', '', '', '']


class entityITICCH(CAResult):
     def __init__(self):
         self.shortname = "ITICCH"
         self.origin = "IT-ICCH-CA-DISCLOSURE.xls"
         self.country = "IT"
         self.bank_specific_notes = "-"
         self.A1= 46223.754
         self.A1_dim= "Mill. EUR"
         self.A2= 32.79
         self.A2_dim= "Mill. EUR"
         self.A3= 1493.9884
         self.A3_dim= "Mill. EUR"
         self.A4= 13480.0
         self.A4_dim= "Mill. EUR"
         self.A5= 50051.7488
         self.A5_dim= "Mill. EUR"
         self.A6= 0.11083
         self.A6_dim= "%"
         self.A7= 0.101799
         self.A7_dim= "%"
         self.A8= 0.101799
         self.A8_dim= "%"
         self.A9= 0.0303
         self.A9_dim= "%"
         self.A10= 0.0476783031729
         self.A10_dim= "%"
         self.A11= 0.332507089408
         self.A11_dim= "%"
         self.A12= 0.00175072323204
         self.A12_dim= "%"
         self.B1= 0.11083
         self.B1_dim= "%"
         self.B2= -44.44
         self.B2_dim= "Basis Points Change"
         self.B3= 0.106386
         self.B3_dim= "%"
         self.B4= 19.4264874804
         self.B4_dim= "Basis Points Change"
         self.B5= 0.108328648748
         self.B5_dim= "%"
         self.B6= -327.865619454
         self.B6_dim= "Basis Points Change"
         self.B7= 0.0735994380546
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#IT-ISP-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'ITISP', '', u'Intesa Sanpaolo S.p.A.', '', '', '', '', '', '', '']


class entityITISP(CAResult):
     def __init__(self):
         self.shortname = "ITISP"
         self.origin = "IT-ISP-CA-DISCLOSURE.xls"
         self.country = "IT"
         self.bank_specific_notes = "-"
         self.A1= 536620.0
         self.A1_dim= "Mill. EUR"
         self.A2= -3858.85824993
         self.A2_dim= "Mill. EUR"
         self.A3= 33992.492
         self.A3_dim= "Mill. EUR"
         self.A4= 284456.0
         self.A4_dim= "Mill. EUR"
         self.A5= 563172.93827
         self.A5_dim= "Mill. EUR"
         self.A6= 0.1195
         self.A6_dim= "%"
         self.A7= 0.12248
         self.A7_dim= "%"
         self.A8= 0.11327
         self.A8_dim= "%"
         self.A9= 0.0624
         self.A9_dim= "%"
         self.A10= 0.0994367157506
         self.A10_dim= "%"
         self.A11= 0.460392863954
         self.A11_dim= "%"
         self.A12= 0.0111877371839
         self.A12_dim= "%"
         self.B1= 0.1195
         self.B1_dim= "%"
         self.B2= -24.61
         self.B2_dim= "Basis Points Change"
         self.B3= 0.117039
         self.B3_dim= "%"
         self.B4= -47.6031810575
         self.B4_dim= "Basis Points Change"
         self.B5= 0.112278681894
         self.B5_dim= "%"
         self.B6= -338.952053915
         self.B6_dim= "Basis Points Change"
         self.B7= 0.0831437946085
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 1756.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#IT-MDB-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'ITMDB', '', u'Mediobanca - Banca di Credito Finanziario S.p.A.', '', '', '', '', '', '', '']


class entityITMDB(CAResult):
     def __init__(self):
         self.shortname = "ITMDB"
         self.origin = "IT-MDB-CA-DISCLOSURE.xls"
         self.country = "IT"
         self.bank_specific_notes = "-"
         self.A1= 75948.156
         self.A1_dim= "Mill. EUR"
         self.A2= -16.679
         self.A2_dim= "Mill. EUR"
         self.A3= 4686.0
         self.A3_dim= "Mill. EUR"
         self.A4= 50640.76
         self.A4_dim= "Mill. EUR"
         self.A5= 71472.6284422
         self.A5_dim= "Mill. EUR"
         self.A6= 0.0925341562804
         self.A6_dim= "%"
         self.A7= 0.1194
         self.A7_dim= "%"
         self.A8= 0.11942
         self.A8_dim= "%"
         self.A9= 0.0655114888563
         self.A9_dim= "%"
         self.A10= 0.031
         self.A10_dim= "%"
         self.A11= 0.424810094131
         self.A11_dim= "%"
         self.A12= 0.0172010232875
         self.A12_dim= "%"
         self.B1= 0.0925341562804
         self.B1_dim= "%"
         self.B2= -85.0
         self.B2_dim= "Basis Points Change"
         self.B3= 0.0840341562804
         self.B3_dim= "%"
         self.B4= 59.7937984943
         self.B4_dim= "Basis Points Change"
         self.B5= 0.0900135361299
         self.B5_dim= "%"
         self.B6= -216.661309241
         self.B6_dim= "Basis Points Change"
         self.B7= 0.0623680253563
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#IT-MPS-CA_DISCLOSURE.xls
#
class entityITMPS(CAResult):
     def __init__(self):
         self.shortname = "ITMPS"
         self.origin = "IT-MPS-CA_DISCLOSURE.xls"
         self.country = "IT"
         self.bank_specific_notes = """- N.B: The Nomura transaction is being treated as a derivative for the purpose of the Comprehensive Assessment. The ECB also notes that the impact of this derivative accounting treatment is regularly disclosed in the published financial statements of MPS.
- Please note that 3000 EUR MM (60%) of "Raising of capital instruments eligible as CET1 capital" and -3000 EUR MM (100%) of "Repayment of CET1 capital, buyback" are already reflected in the Stress Test outcome. Therefore only the remaining 2000 EUR MM raised should be considered as additional capital following the Comprehensive Assessment result.
- Please note: the AQR-adjusted CET1 Ratio (item B3 in the sheet ‘Main Results and Overview’) includes both the impact of the AQR, and an adjustment due to IRB provisioning shortfall. The IRB provisioning shortfall adjustment is not presented in the sheet ‘Detailed AQR Results’. """
         self.A1= 199105.905787
         self.A1_dim= "Mill. EUR"
         self.A2= -1439.043372
         self.A2_dim= "Mill. EUR"
         self.A3= 8504.578612
         self.A3_dim= "Mill. EUR"
         self.A4= 83492.0
         self.A4_dim= "Mill. EUR"
         self.A5= 207423.410648
         self.A5_dim= "Mill. EUR"
         self.A6= 0.101861
         self.A6_dim= "%"
         self.A7= 0.1062
         self.A7_dim= "%"
         self.A8= 0.09886
         self.A8_dim= "%"
         self.A9= 0.0429588148809
         self.A9_dim= "%"
         self.A10= 0.181120677514
         self.A10_dim= "%"
         self.A11= 0.400942178516
         self.A11_dim= "%"
         self.A12= 0.00346850585506
         self.A12_dim= "%"
         self.B1= 0.101861
         self.B1_dim= "%"
         self.B2= -319.861884481
         self.B2_dim= "Basis Points Change"
         self.B3= 0.0698748115519
         self.B3_dim= "%"
         self.B4= -97.4196064631
         self.B4_dim= "Basis Points Change"
         self.B5= 0.0601328509056
         self.B5_dim= "%"
         self.B6= -708.1672991
         self.B6_dim= "Basis Points Change"
         self.B7= -0.00094191835811
         self.B7_dim= "%"
         self.B8= 101.251884481
         self.B9= 198.671490944
         self.B10= 559.419183581
         self.B11= 559.419183581
         self.C1= 5138.75
         self.C2= -3000.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= -63.06



#IT-UBI-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'ITUBI', '', u'Unione Di Banche Italiane Societ\xe0 Cooperativa Per Azioni', '', '', '', '', '', '', '']


class entityITUBI(CAResult):
     def __init__(self):
         self.shortname = "ITUBI"
         self.origin = "IT-UBI-CA-DISCLOSURE.xls"
         self.country = "IT"
         self.bank_specific_notes = "-"
         self.A1= 124286.0
         self.A1_dim= "Mill. EUR"
         self.A2= 251.0
         self.A2_dim= "Mill. EUR"
         self.A3= 7786.776226
         self.A3_dim= "Mill. EUR"
         self.A4= 63540.104168
         self.A4_dim= "Mill. EUR"
         self.A5= 129711.0
         self.A5_dim= "Mill. EUR"
         self.A6= 0.122549000005
         self.A6_dim= "%"
         self.A7= 0.132282
         self.A7_dim= "%"
         self.A8= 0.126011
         self.A8_dim= "%"
         self.A9= 0.0535
         self.A9_dim= "%"
         self.A10= 0.109468378458
         self.A10_dim= "%"
         self.A11= 0.327483286457
         self.A11_dim= "%"
         self.A12= 0.0022
         self.A12_dim= "%"
         self.B1= 0.122549000005
         self.B1_dim= "%"
         self.B2= -43.51
         self.B2_dim= "Basis Points Change"
         self.B3= 0.118198000005
         self.B3_dim= "%"
         self.B4= -93.5874346603
         self.B4_dim= "Basis Points Change"
         self.B5= 0.108839256539
         self.B5_dim= "%"
         self.B6= -361.688596908
         self.B6_dim= "Basis Points Change"
         self.B7= 0.0820291403142
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 18.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#IT-UCG-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'ITUCG', '', u'UniCredit S.p.A.', '', '', '', '', '', '', '']


class entityITUCG(CAResult):
     def __init__(self):
         self.shortname = "ITUCG"
         self.origin = "IT-UCG-CA-DISCLOSURE.xls"
         self.country = "IT"
         self.bank_specific_notes = "-"
         self.A1= 849993.02
         self.A1_dim= "Mill. EUR"
         self.A2= -13964.832
         self.A2_dim= "Mill. EUR"
         self.A3= 39899.613992
         self.A3_dim= "Mill. EUR"
         self.A4= 408587.158299
         self.A4_dim= "Mill. EUR"
         self.A5= 888539.854028
         self.A5_dim= "Mill. EUR"
         self.A6= 0.0976526383211
         self.A6_dim= "%"
         self.A7= 0.1009
         self.A7_dim= "%"
         self.A8= 0.09601
         self.A8_dim= "%"
         self.A9= 0.0469767322379
         self.A9_dim= "%"
         self.A10= 0.106291022095
         self.A10_dim= "%"
         self.A11= 0.500753444209
         self.A11_dim= "%"
         self.A12= 0.00778816395457
         self.A12_dim= "%"
         self.B1= 0.0976526383211
         self.B1_dim= "%"
         self.B2= -18.75
         self.B2_dim= "Basis Points Change"
         self.B3= 0.0957776383211
         self.B3_dim= "%"
         self.B4= -7.94656434226
         self.B4_dim= "Basis Points Change"
         self.B5= 0.0949829818868
         self.B5_dim= "%"
         self.B6= -279.043803864
         self.B6_dim= "Basis Points Change"
         self.B7= 0.0678732579347
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 1234.9157
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#IT-VENE-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'ITVENE', '', u'Veneto Banca S.C.P.A.', '', '', '', '', '', '', '']


class entityITVENE(CAResult):
     def __init__(self):
         self.shortname = "ITVENE"
         self.origin = "IT-VENE-CA-DISCLOSURE.xls"
         self.country = "IT"
         self.bank_specific_notes = "-"
         self.A1= 37105.0
         self.A1_dim= "Mill. EUR"
         self.A2= -100.0
         self.A2_dim= "Mill. EUR"
         self.A3= 1844.38691
         self.A3_dim= "Mill. EUR"
         self.A4= 25166.701611
         self.A4_dim= "Mill. EUR"
         self.A5= 39639.0
         self.A5_dim= "Mill. EUR"
         self.A6= 0.0732867953262
         self.A6_dim= "%"
         self.A7= 0.078734
         self.A7_dim= "%"
         self.A8= 0.07334
         self.A8_dim= "%"
         self.A9= 0.0502
         self.A9_dim= "%"
         self.A10= 0.113
         self.A10_dim= "%"
         self.A11= 0.3018
         self.A11_dim= "%"
         self.A12= 0.0138
         self.A12_dim= "%"
         self.B1= 0.0732867953262
         self.B1_dim= "%"
         self.B2= -162.94
         self.B2_dim= "Basis Points Change"
         self.B3= 0.0569927953262
         self.B3_dim= "%"
         self.B4= 7.57700523664
         self.B4_dim= "Basis Points Change"
         self.B5= 0.0577504958498
         self.B5_dim= "%"
         self.B6= -296.435469728
         self.B6_dim= "Basis Points Change"
         self.B7= 0.0273492483533
         self.B7_dim= "%"
         self.B8= 230.07
         self.B9= 222.492994763
         self.B10= 276.505469728
         self.B11= 276.505469728
         self.C1= 483.16
         self.C2= -99.09
         self.C3= 353.74
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= -7.85088

#LT-DNBB-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'LTDNBB', '', u'AB DNB bankas', '', '', '', '', '', '', '']


class entityLTDNBB(CAResult):
     def __init__(self):
         self.shortname = "LTDNBB"
         self.origin = "LT-DNBB-CA-DISCLOSURE.xls"
         self.country = "LT"
         self.bank_specific_notes = "-"
         self.A1= 3468.05
         self.A1_dim= "Mill. EUR"
         self.A2= 13.0
         self.A2_dim= "Mill. EUR"
         self.A3= 398.351
         self.A3_dim= "Mill. EUR"
         self.A4= 2335.0
         self.A4_dim= "Mill. EUR"
         self.A5= 3870.0
         self.A5_dim= "Mill. EUR"
         self.A6= 0.1706
         self.A6_dim= "%"
         self.A7= 0.1675
         self.A7_dim= "%"
         self.A8= 0.167546
         self.A8_dim= "%"
         self.A9= 0.102842
         self.A9_dim= "%"
         self.A10= 0.152489063177
         self.A10_dim= "%"
         self.A11= 0.333159737678
         self.A11_dim= "%"
         self.A12= 0.003
         self.A12_dim= "%"
         self.B1= 0.1706
         self.B1_dim= "%"
         self.B2= -72.02
         self.B2_dim= "Basis Points Change"
         self.B3= 0.163398
         self.B3_dim= "%"
         self.B4= -10.3760814994
         self.B4_dim= "Basis Points Change"
         self.B5= 0.16236039185
         self.B5_dim= "%"
         self.B6= -359.47387793
         self.B6_dim= "Basis Points Change"
         self.B7= 0.127450612207
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#LT-SEBB-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'LTSEBB', '', u'AB SEB bankas', '', '', '', '', '', '', '']


class entityLTSEBB(CAResult):
     def __init__(self):
         self.shortname = "LTSEBB"
         self.origin = "LT-SEBB-CA-DISCLOSURE.xls"
         self.country = "LT"
         self.bank_specific_notes = "-"
         self.A1= 6834.53544949
         self.A1_dim= "Mill. EUR"
         self.A2= 61.52601
         self.A2_dim= "Mill. EUR"
         self.A3= 678.166995
         self.A3_dim= "Mill. EUR"
         self.A4= 4414.737293
         self.A4_dim= "Mill. EUR"
         self.A5= 8274.791694
         self.A5_dim= "Mill. EUR"
         self.A6= 0.153614348939
         self.A6_dim= "%"
         self.A7= 0.1559
         self.A7_dim= "%"
         self.A8= 0.15588
         self.A8_dim= "%"
         self.A9= 0.0819557784632
         self.A9_dim= "%"
         self.A10= 0.0681277559117
         self.A10_dim= "%"
         self.A11= 0.47721807675
         self.A11_dim= "%"
         self.A12= 0.00189
         self.A12_dim= "%"
         self.B1= 0.153614348939
         self.B1_dim= "%"
         self.B2= -49.25
         self.B2_dim= "Basis Points Change"
         self.B3= 0.148689348939
         self.B3_dim= "%"
         self.B4= 2.33353583774
         self.B4_dim= "Basis Points Change"
         self.B5= 0.148922702523
         self.B5_dim= "%"
         self.B6= -153.71273618
         self.B6_dim= "Basis Points Change"
         self.B7= 0.133318075321
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#LT-SWBK-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'LTSWBK', '', u'Swedbank AB', '', '', '', '', '', '', '']


class entityLTSWBK(CAResult):
     def __init__(self):
         self.shortname = "LTSWBK"
         self.origin = "LT-SWBK-CA-DISCLOSURE.xls"
         self.country = "LT"
         self.bank_specific_notes = "-"
         self.A1= 5672.0
         self.A1_dim= "Mill. EUR"
         self.A2= 114.0
         self.A2_dim= "Mill. EUR"
         self.A3= 792.9572
         self.A3_dim= "Mill. EUR"
         self.A4= 3518.0
         self.A4_dim= "Mill. EUR"
         self.A5= 5305.0
         self.A5_dim= "Mill. EUR"
         self.A6= 0.2254
         self.A6_dim= "%"
         self.A7= 0.223
         self.A7_dim= "%"
         self.A8= 0.222958
         self.A8_dim= "%"
         self.A9= 0.1495
         self.A9_dim= "%"
         self.A10= 0.035081250169
         self.A10_dim= "%"
         self.A11= 0.415420884963
         self.A11_dim= "%"
         self.A12= 0.0
         self.A12_dim= "%"
         self.B1= 0.2254
         self.B1_dim= "%"
         self.B2= -15.02
         self.B2_dim= "Basis Points Change"
         self.B3= 0.223898
         self.B3_dim= "%"
         self.B4= 81.4350823527
         self.B4_dim= "Basis Points Change"
         self.B5= 0.232041508235
         self.B5_dim= "%"
         self.B6= 46.2513573822
         self.B6_dim= "Basis Points Change"
         self.B7= 0.228523135738
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#LU-BCEE-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'LUBCEE', '', u"Banque et Caisse d'Epargne de l'Etat, Luxembourg", '', '', '', '', '', '', '']


class entityLUBCEE(CAResult):
     def __init__(self):
         self.shortname = "LUBCEE"
         self.origin = "LU-BCEE-CA-DISCLOSURE.xls"
         self.country = "LU"
         self.bank_specific_notes = "-"
         self.A1= 40664.0
         self.A1_dim= "Mill. EUR"
         self.A2= 208.0
         self.A2_dim= "Mill. EUR"
         self.A3= 2374.12523
         self.A3_dim= "Mill. EUR"
         self.A4= 13884.997369
         self.A4_dim= "Mill. EUR"
         self.A5= 42960.0
         self.A5_dim= "Mill. EUR"
         self.A6= 0.170984924729
         self.A6_dim= "%"
         self.A7= 0.166442
         self.A7_dim= "%"
         self.A8= 0.166442
         self.A8_dim= "%"
         self.A9= 0.0723
         self.A9_dim= "%"
         self.A10= 0.0127
         self.A10_dim= "%"
         self.A11= 0.3379
         self.A11_dim= "%"
         self.A12= 0.0111
         self.A12_dim= "%"
         self.B1= 0.170984924729
         self.B1_dim= "%"
         self.B2= -5.85
         self.B2_dim= "Basis Points Change"
         self.B3= 0.170399924729
         self.B3_dim= "%"
         self.B4= -166.153298545
         self.B4_dim= "Basis Points Change"
         self.B5= 0.153784594874
         self.B5_dim= "%"
         self.B6= -418.901668725
         self.B6_dim= "Basis Points Change"
         self.B7= 0.128509757856
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#LU-CLST-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'LUCLST', '', u'Clearstream Banking S.A.', '', '', '', '', '', '', '']


class entityLUCLST(CAResult):
     def __init__(self):
         self.shortname = "LUCLST"
         self.origin = "LU-CLST-CA-DISCLOSURE.xls"
         self.country = "LU"
         self.bank_specific_notes = "-"
         self.A1= 11246.8
         self.A1_dim= "Mill. EUR"
         self.A2= 19.1
         self.A2_dim= "Mill. EUR"
         self.A3= 651.8
         self.A3_dim= "Mill. EUR"
         self.A4= 3363.0
         self.A4_dim= "Mill. EUR"
         self.A5= 11246.0
         self.A5_dim= "Mill. EUR"
         self.A6= 0.19381504609
         self.A6_dim= "%"
         self.A7= 0.1931
         self.A7_dim= "%"
         self.A8= 0.193131
         self.A8_dim= "%"
         self.A9= 0.0579
         self.A9_dim= "%"
         self.A10= 0.0
         self.A10_dim= "%"
         self.A11= 0.0
         self.A11_dim= "%"
         self.A12= 0.0003
         self.A12_dim= "%"
         self.B1= 0.19381504609
         self.B1_dim= "%"
         self.B2= 0.0
         self.B2_dim= "Basis Points Change"
         self.B3= 0.19381504609
         self.B3_dim= "%"
         self.B4= -12.3309428456
         self.B4_dim= "Basis Points Change"
         self.B5= 0.192581951805
         self.B5_dim= "%"
         self.B6= -147.236094498
         self.B6_dim= "Basis Points Change"
         self.B7= 0.17909143664
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 240.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#LU-PCAP-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'LUPCAP', '', u'Precision Capital S.A. (Holding of Banque Internationale \xe0 Luxembourg ', '', '', '', '', '', '', '']


class entityLUPCAP(CAResult):
     def __init__(self):
         self.shortname = "LUPCAP"
         self.origin = "LU-PCAP-CA-DISCLOSURE.xls"
         self.country = "LU"
         self.bank_specific_notes = "-"
         self.A1= 32483.0
         self.A1_dim= "Mill. EUR"
         self.A2= 139.0
         self.A2_dim= "Mill. EUR"
         self.A3= 1272.619282
         self.A3_dim= "Mill. EUR"
         self.A4= 8622.128536
         self.A4_dim= "Mill. EUR"
         self.A5= 28590.0
         self.A5_dim= "Mill. EUR"
         self.A6= 0.147599200903
         self.A6_dim= "%"
         self.A7= 0.136132
         self.A7_dim= "%"
         self.A8= 0.136132
         self.A8_dim= "%"
         self.A9= 0.0445
         self.A9_dim= "%"
         self.A10= 0.0258
         self.A10_dim= "%"
         self.A11= 0.3621
         self.A11_dim= "%"
         self.A12= 0.0024
         self.A12_dim= "%"
         self.B1= 0.147599200903
         self.B1_dim= "%"
         self.B2= -74.2
         self.B2_dim= "Basis Points Change"
         self.B3= 0.140179200903
         self.B3_dim= "%"
         self.B4= -152.617401007
         self.B4_dim= "Basis Points Change"
         self.B5= 0.124917460803
         self.B5_dim= "%"
         self.B6= -572.401309518
         self.B6_dim= "Basis Points Change"
         self.B7= 0.0829390699516
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 150.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= -8.0

#LU-RBC-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'LURBC', '', u'RBC Investor Services Bank S.A.', '', '', '', '', '', '', '']


class entityLURBC(CAResult):
     def __init__(self):
         self.shortname = "LURBC"
         self.origin = "LU-RBC-CA-DISCLOSURE.xls"
         self.country = "LU"
         self.bank_specific_notes = "-"
         self.A1= 12743.0
         self.A1_dim= "Mill. EUR"
         self.A2= 11.0
         self.A2_dim= "Mill. EUR"
         self.A3= 741.958167
         self.A3_dim= "Mill. EUR"
         self.A4= 2859.794455
         self.A4_dim= "Mill. EUR"
         self.A5= 13210.75
         self.A5_dim= "Mill. EUR"
         self.A6= 0.259444578509
         self.A6_dim= "%"
         self.A7= 0.2999
         self.A7_dim= "%"
         self.A8= 0.299861
         self.A8_dim= "%"
         self.A9= 0.0562
         self.A9_dim= "%"
         self.A10= 0.0
         self.A10_dim= "%"
         self.A11= 0.0
         self.A11_dim= "%"
         self.A12= 0.0
         self.A12_dim= "%"
         self.B1= 0.259444578509
         self.B1_dim= "%"
         self.B2= 0.0
         self.B2_dim= "Basis Points Change"
         self.B3= 0.259444578509
         self.B3_dim= "%"
         self.B4= -562.01242849
         self.B4_dim= "Basis Points Change"
         self.B5= 0.20324333566
         self.B5_dim= "%"
         self.B6= -1297.13652501
         self.B6_dim= "Basis Points Change"
         self.B7= 0.129730926008
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#LU-STST-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'LUSTST', '', u'State Street Bank Luxembourg S.A.', '', '', '', '', '', '', '']


class entityLUSTST(CAResult):
     def __init__(self):
         self.shortname = "LUSTST"
         self.origin = "LU-STST-CA-DISCLOSURE.xls"
         self.country = "LU"
         self.bank_specific_notes = "-"
         self.A1= 31362.4709032
         self.A1_dim= "Mill. EUR"
         self.A2= 193.43883245
         self.A2_dim= "Mill. EUR"
         self.A3= 1473.842353
         self.A3_dim= "Mill. EUR"
         self.A4= 6161.526625
         self.A4_dim= "Mill. EUR"
         self.A5= 12136.4681325
         self.A5_dim= "Mill. EUR"
         self.A6= 0.239200841399
         self.A6_dim= "%"
         self.A7= 0.2061
         self.A7_dim= "%"
         self.A8= 0.206064
         self.A8_dim= "%"
         self.A9= 0.121439073424
         self.A9_dim= "%"
         self.A10= 0.000186633602566
         self.A10_dim= "%"
         self.A11= 0.300276948718
         self.A11_dim= "%"
         self.A12= 0.0196911680813
         self.A12_dim= "%"
         self.B1= 0.239200841399
         self.B1_dim= "%"
         self.B2= -18.86
         self.B2_dim= "Basis Points Change"
         self.B3= 0.237314841399
         self.B3_dim= "%"
         self.B4= 155.349917957
         self.B4_dim= "Basis Points Change"
         self.B5= 0.252849833194
         self.B5_dim= "%"
         self.B6= -144.28860225
         self.B6_dim= "Basis Points Change"
         self.B7= 0.222885981174
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#LU-UBS-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'LUUBS', '', u'UBS (Luxembourg) S.A.', '', '', '', '', '', '', '']


class entityLUUBS(CAResult):
     def __init__(self):
         self.shortname = "LUUBS"
         self.origin = "LU-UBS-CA-DISCLOSURE.xls"
         self.country = "LU"
         self.bank_specific_notes = "-"
         self.A1= 10095.0
         self.A1_dim= "Mill. EUR"
         self.A2= 40.0
         self.A2_dim= "Mill. EUR"
         self.A3= 458.73
         self.A3_dim= "Mill. EUR"
         self.A4= 3288.0
         self.A4_dim= "Mill. EUR"
         self.A5= 10081.0
         self.A5_dim= "Mill. EUR"
         self.A6= 0.139516423358
         self.A6_dim= "%"
         self.A7= 0.152
         self.A7_dim= "%"
         self.A8= 0.152013
         self.A8_dim= "%"
         self.A9= 0.0486
         self.A9_dim= "%"
         self.A10= 0.0002
         self.A10_dim= "%"
         self.A11= 0.9978
         self.A11_dim= "%"
         self.A12= 3e-12
         self.A12_dim= "%"
         self.B1= 0.139516423358
         self.B1_dim= "%"
         self.B2= 0.0
         self.B2_dim= "Basis Points Change"
         self.B3= 0.139516423358
         self.B3_dim= "%"
         self.B4= -198.604779125
         self.B4_dim= "Basis Points Change"
         self.B5= 0.119655945445
         self.B5_dim= "%"
         self.B6= -404.447135757
         self.B6_dim= "Basis Points Change"
         self.B7= 0.099071709782
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#LV-ABLV-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'LVABLV', '', u'ABLV Bank, AS', '', '', '', '', '', '', '']


class entityLVABLV(CAResult):
     def __init__(self):
         self.shortname = "LVABLV"
         self.origin = "LV-ABLV-CA-DISCLOSURE.xls"
         self.country = "LV"
         self.bank_specific_notes = "-"
         self.A1= 3306.0
         self.A1_dim= "Mill. EUR"
         self.A2= 51.0
         self.A2_dim= "Mill. EUR"
         self.A3= 166.14571
         self.A3_dim= "Mill. EUR"
         self.A4= 1599.092492
         self.A4_dim= "Mill. EUR"
         self.A5= 3358.0
         self.A5_dim= "Mill. EUR"
         self.A6= 0.103900000051
         self.A6_dim= "%"
         self.A7= 0.0967
         self.A7_dim= "%"
         self.A8= 0.096709
         self.A8_dim= "%"
         self.A9= 0.0496558067302
         self.A9_dim= "%"
         self.A10= 0.0396
         self.A10_dim= "%"
         self.A11= 0.4686
         self.A11_dim= "%"
         self.A12= 0.0435
         self.A12_dim= "%"
         self.B1= 0.103900000051
         self.B1_dim= "%"
         self.B2= -63.72
         self.B2_dim= "Basis Points Change"
         self.B3= 0.0975280000508
         self.B3_dim= "%"
         self.B4= 2.45552027045
         self.B4_dim= "Basis Points Change"
         self.B5= 0.0977735520778
         self.B5_dim= "%"
         self.B6= -209.668334743
         self.B6_dim= "Basis Points Change"
         self.B7= 0.0765611665765
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#LV-SEB-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'LVSEB', '', u'AS SEB banka', '', '', '', '', '', '', '']


class entityLVSEB(CAResult):
     def __init__(self):
         self.shortname = "LVSEB"
         self.origin = "LV-SEB-CA-DISCLOSURE.xls"
         self.country = "LV"
         self.bank_specific_notes = "-"
         self.A1= 4276.0
         self.A1_dim= "Mill. EUR"
         self.A2= 26.0
         self.A2_dim= "Mill. EUR"
         self.A3= 392.70375
         self.A3_dim= "Mill. EUR"
         self.A4= 2565.014697
         self.A4_dim= "Mill. EUR"
         self.A5= 4484.0
         self.A5_dim= "Mill. EUR"
         self.A6= 0.153099999957
         self.A6_dim= "%"
         self.A7= 0.1511
         self.A7_dim= "%"
         self.A8= 0.1511
         self.A8_dim= "%"
         self.A9= 0.0886
         self.A9_dim= "%"
         self.A10= 0.0534748697626
         self.A10_dim= "%"
         self.A11= 0.391950461968
         self.A11_dim= "%"
         self.A12= 0.1
         self.A12_dim= "%"
         self.B1= 0.153099999957
         self.B1_dim= "%"
         self.B2= -202.0
         self.B2_dim= "Basis Points Change"
         self.B3= 0.132899999957
         self.B3_dim= "%"
         self.B4= -13.3999785358
         self.B4_dim= "Basis Points Change"
         self.B5= 0.131560002103
         self.B5_dim= "%"
         self.B6= -139.414447554
         self.B6_dim= "Basis Points Change"
         self.B7= 0.118958555201
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#LV-SWED-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'LVSWED', '', u'Swedbank AS', '', '', '', '', '', '', '']


class entityLVSWED(CAResult):
     def __init__(self):
         self.shortname = "LVSWED"
         self.origin = "LV-SWED-CA-DISCLOSURE.xls"
         self.country = "LV"
         self.bank_specific_notes = "-"
         self.A1= 5052.96
         self.A1_dim= "Mill. EUR"
         self.A2= 112.94
         self.A2_dim= "Mill. EUR"
         self.A3= 997.277526
         self.A3_dim= "Mill. EUR"
         self.A4= 3058.421
         self.A4_dim= "Mill. EUR"
         self.A5= 5537.03
         self.A5_dim= "Mill. EUR"
         self.A6= 0.326075947687
         self.A6_dim= "%"
         self.A7= 0.280574
         self.A7_dim= "%"
         self.A8= 0.280574
         self.A8_dim= "%"
         self.A9= 0.1801
         self.A9_dim= "%"
         self.A10= 0.0433
         self.A10_dim= "%"
         self.A11= 0.6475
         self.A11_dim= "%"
         self.A12= 0.0
         self.A12_dim= "%"
         self.B1= 0.326075947687
         self.B1_dim= "%"
         self.B2= -19.2
         self.B2_dim= "Basis Points Change"
         self.B3= 0.324155947687
         self.B3_dim= "%"
         self.B4= -28.3500539324
         self.B4_dim= "Basis Points Change"
         self.B5= 0.321320942293
         self.B5_dim= "%"
         self.B6= -62.0232213526
         self.B6_dim= "Basis Points Change"
         self.B7= 0.317953625551
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#MT-CBOV-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'MTCBOV', '', u'Bank of Valletta plc', '', '', '', '', '', '', '']


class entityMTCBOV(CAResult):
     def __init__(self):
         self.shortname = "MTCBOV"
         self.origin = "MT-CBOV-CA-DISCLOSURE.xls"
         self.country = "MT"
         self.bank_specific_notes = "-"
         self.A1= 7425.022
         self.A1_dim= "Mill. EUR"
         self.A2= 65.2859551
         self.A2_dim= "Mill. EUR"
         self.A3= 408.410464
         self.A3_dim= "Mill. EUR"
         self.A4= 3646.522
         self.A4_dim= "Mill. EUR"
         self.A5= 7704.62696405
         self.A5_dim= "Mill. EUR"
         self.A6= 0.112
         self.A6_dim= "%"
         self.A7= 0.1148
         self.A7_dim= "%"
         self.A8= 0.114776
         self.A8_dim= "%"
         self.A9= 0.0530415258508
         self.A9_dim= "%"
         self.A10= 0.0452743474092
         self.A10_dim= "%"
         self.A11= 0.520979377919
         self.A11_dim= "%"
         self.A12= 0.0
         self.A12_dim= "%"
         self.B1= 0.112
         self.B1_dim= "%"
         self.B2= -49.1
         self.B2_dim= "Basis Points Change"
         self.B3= 0.10709
         self.B3_dim= "%"
         self.B4= 122.164365009
         self.B4_dim= "Basis Points Change"
         self.B5= 0.119306436501
         self.B5_dim= "%"
         self.B6= -179.096245155
         self.B6_dim= "Basis Points Change"
         self.B7= 0.0891803754845
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#MT-CHSBC-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'MTCHSBC', '', u'HSBC Bank Malta plc', '', '', '', '', '', '', '']


class entityMTCHSBC(CAResult):
     def __init__(self):
         self.shortname = "MTCHSBC"
         self.origin = "MT-CHSBC-CA-DISCLOSURE.xls"
         self.country = "MT"
         self.bank_specific_notes = "-"
         self.A1= 5127.9709367
         self.A1_dim= "Mill. EUR"
         self.A2= 57.845
         self.A2_dim= "Mill. EUR"
         self.A3= 279.816017
         self.A3_dim= "Mill. EUR"
         self.A4= 2824.740574
         self.A4_dim= "Mill. EUR"
         self.A5= 5355.57345557
         self.A5_dim= "Mill. EUR"
         self.A6= 0.0990590143306
         self.A6_dim= "%"
         self.A7= 0.094219
         self.A7_dim= "%"
         self.A8= 0.094219
         self.A8_dim= "%"
         self.A9= 0.0522819829329
         self.A9_dim= "%"
         self.A10= 0.0599265984478
         self.A10_dim= "%"
         self.A11= 0.231
         self.A11_dim= "%"
         self.A12= 0.0
         self.A12_dim= "%"
         self.B1= 0.0990590143306
         self.B1_dim= "%"
         self.B2= -88.85
         self.B2_dim= "Basis Points Change"
         self.B3= 0.0901740143306
         self.B3_dim= "%"
         self.B4= 24.4095605818
         self.B4_dim= "Basis Points Change"
         self.B5= 0.0926149703887
         self.B5_dim= "%"
         self.B6= -10.5831858017
         self.B6_dim= "Basis Points Change"
         self.B7= 0.0891156957504
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#MT-DB-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'MTDB', '', u'Deutsche Bank (Malta) Ltd', '', '', '', '', '', '', '']


class entityMTDB(CAResult):
     def __init__(self):
         self.shortname = "MTDB"
         self.origin = "MT-DB-CA-DISCLOSURE.xls"
         self.country = "MT"
         self.bank_specific_notes = "-"
         self.A1= 2831.0
         self.A1_dim= "Mill. EUR"
         self.A2= 43.7
         self.A2_dim= "Mill. EUR"
         self.A3= 2228.1252
         self.A3_dim= "Mill. EUR"
         self.A4= 791.8
         self.A4_dim= "Mill. EUR"
         self.A5= 2831.0
         self.A5_dim= "Mill. EUR"
         self.A6= 2.814
         self.A6_dim= "%"
         self.A7= 2.814
         self.A7_dim= "%"
         self.A8= 2.814047
         self.A8_dim= "%"
         self.A9= 0.787001059696
         self.A9_dim= "%"
         self.A10= 0.0
         self.A10_dim= "%"
         self.A11= 0.0
         self.A11_dim= "%"
         self.A12= 0.0
         self.A12_dim= "%"
         self.B1= 2.814
         self.B1_dim= "%"
         self.B2= 0.0
         self.B2_dim= "Basis Points Change"
         self.B3= 2.814
         self.B3_dim= "%"
         self.B4= -80.2092205001
         self.B4_dim= "Basis Points Change"
         self.B5= 2.80597907795
         self.B5_dim= "%"
         self.B6= -14263.8678348
         self.B6_dim= "Basis Points Change"
         self.B7= 1.38761321652
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= -2204.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#NL-ABN-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'NLABN', '', u'ABN Amro Bank N.V.', '', '', '', '', '', '', '']


class entityNLABN(CAResult):
     def __init__(self):
         self.shortname = "NLABN"
         self.origin = "NL-ABN-CA-DISCLOSURE.xls"
         self.country = "NL"
         self.bank_specific_notes = "-"
         self.A1= 369752.0
         self.A1_dim= "Mill. EUR"
         self.A2= 927.0
         self.A2_dim= "Mill. EUR"
         self.A3= 14119.584602
         self.A3_dim= "Mill. EUR"
         self.A4= 115442.095578
         self.A4_dim= "Mill. EUR"
         self.A5= 448066.0
         self.A5_dim= "Mill. EUR"
         self.A6= 0.122308803659
         self.A6_dim= "%"
         self.A7= 0.135766
         self.A7_dim= "%"
         self.A8= 0.126593
         self.A8_dim= "%"
         self.A9= 0.0325911807635
         self.A9_dim= "%"
         self.A10= 0.0284868161473
         self.A10_dim= "%"
         self.A11= 0.502155323571
         self.A11_dim= "%"
         self.A12= 0.00357266492135
         self.A12_dim= "%"
         self.B1= 0.122308803659
         self.B1_dim= "%"
         self.B2= -12.32
         self.B2_dim= "Basis Points Change"
         self.B3= 0.121076803659
         self.B3_dim= "%"
         self.B4= 34.635691139
         self.B4_dim= "Basis Points Change"
         self.B5= 0.124540372773
         self.B5_dim= "%"
         self.B6= -296.16804273
         self.B6_dim= "Basis Points Change"
         self.B7= 0.0914599993857
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#NL-GEM-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'NLGEM', '', u'Bank Nederlandse Gemeenten N.V.', '', '', '', '', '', '', '']


class entityNLGEM(CAResult):
     def __init__(self):
         self.shortname = "NLGEM"
         self.origin = "NL-GEM-CA-DISCLOSURE.xls"
         self.country = "NL"
         self.bank_specific_notes = "-"
         self.A1= 131183.0
         self.A1_dim= "Mill. EUR"
         self.A2= 283.0
         self.A2_dim= "Mill. EUR"
         self.A3= 2767.29
         self.A3_dim= "Mill. EUR"
         self.A4= 11663.49
         self.A4_dim= "Mill. EUR"
         self.A5= 119427.0
         self.A5_dim= "Mill. EUR"
         self.A6= 0.237260888465
         self.A6_dim= "%"
         self.A7= 0.2439
         self.A7_dim= "%"
         self.A8= 0.243585
         self.A8_dim= "%"
         self.A9= 0.0247
         self.A9_dim= "%"
         self.A10= 0.001
         self.A10_dim= "%"
         self.A11= 0.3985
         self.A11_dim= "%"
         self.A12= 0.0097
         self.A12_dim= "%"
         self.B1= 0.237260888465
         self.B1_dim= "%"
         self.B2= -187.54
         self.B2_dim= "Basis Points Change"
         self.B3= 0.218506888465
         self.B3_dim= "%"
         self.B4= -52.5698762594
         self.B4_dim= "Basis Points Change"
         self.B5= 0.213249900839
         self.B5_dim= "%"
         self.B6= -458.370898691
         self.B6_dim= "Basis Points Change"
         self.B7= 0.172669798596
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#NL-ING-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'NLING', '', u'ING Bank N.V.', '', '', '', '', '', '', '']


class entityNLING(CAResult):
     def __init__(self):
         self.shortname = "NLING"
         self.origin = "NL-ING-CA-DISCLOSURE.xls"
         self.country = "NL"
         self.bank_specific_notes = "-"
         self.A1= 786504.0
         self.A1_dim= "Mill. EUR"
         self.A2= 3119.0
         self.A2_dim= "Mill. EUR"
         self.A3= 30919.482165
         self.A3_dim= "Mill. EUR"
         self.A4= 297958.0
         self.A4_dim= "Mill. EUR"
         self.A5= 1020845.0
         self.A5_dim= "Mill. EUR"
         self.A6= 0.103771277042
         self.A6_dim= "%"
         self.A7= 0.1353
         self.A7_dim= "%"
         self.A8= 0.106695
         self.A8_dim= "%"
         self.A9= 0.0335
         self.A9_dim= "%"
         self.A10= 0.0263
         self.A10_dim= "%"
         self.A11= 0.3851
         self.A11_dim= "%"
         self.A12= 0.00330703976076
         self.A12_dim= "%"
         self.B1= 0.103771277042
         self.B1_dim= "%"
         self.B2= -29.0
         self.B2_dim= "Basis Points Change"
         self.B3= 0.100871277042
         self.B3_dim= "%"
         self.B4= 32.278146595
         self.B4_dim= "Basis Points Change"
         self.B5= 0.104099091702
         self.B5_dim= "%"
         self.B6= -143.478972583
         self.B6_dim= "Basis Points Change"
         self.B7= 0.0865233797841
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#NL-NWNV-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'NLNWNV', '', u'Nederlandse Waterschapsbank N.V.', '', '', '', '', '', '', '']


class entityNLNWNV(CAResult):
     def __init__(self):
         self.shortname = "NLNWNV"
         self.origin = "NL-NWNV-CA-DISCLOSURE.xls"
         self.country = "NL"
         self.bank_specific_notes = "-"
         self.A1= 73006.0
         self.A1_dim= "Mill. EUR"
         self.A2= 34.0
         self.A2_dim= "Mill. EUR"
         self.A3= 1261.196205
         self.A3_dim= "Mill. EUR"
         self.A4= 1669.3485
         self.A4_dim= "Mill. EUR"
         self.A5= 71210.0
         self.A5_dim= "Mill. EUR"
         self.A6= 0.75550204466
         self.A6_dim= "%"
         self.A7= 1.0089
         self.A7_dim= "%"
         self.A8= 1.00888
         self.A8_dim= "%"
         self.A9= 0.0176
         self.A9_dim= "%"
         self.A10= 0.0
         self.A10_dim= "%"
         self.A11= 0.0
         self.A11_dim= "%"
         self.A12= 0.000103198965946
         self.A12_dim= "%"
         self.B1= 0.75550204466
         self.B1_dim= "%"
         self.B2= -303.88
         self.B2_dim= "Basis Points Change"
         self.B3= 0.72511404466
         self.B3_dim= "%"
         self.B4= 5.50814010113
         self.B4_dim= "Basis Points Change"
         self.B5= 0.72566485867
         self.B5_dim= "%"
         self.B6= -1849.29084597
         self.B6_dim= "Basis Points Change"
         self.B7= 0.540184960063
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#NL-RABO-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'NLRABO', '', u'Co\xf6peratieve Centrale Raiffeisen-Boerenleenbank B.A.', '', '', '', '', '', '', '']


class entityNLRABO(CAResult):
     def __init__(self):
         self.shortname = "NLRABO"
         self.origin = "NL-RABO-CA-DISCLOSURE.xls"
         self.country = "NL"
         self.bank_specific_notes = "-"
         self.A1= 674139.0
         self.A1_dim= "Mill. EUR"
         self.A2= 2012.0
         self.A2_dim= "Mill. EUR"
         self.A3= 26832.4
         self.A3_dim= "Mill. EUR"
         self.A4= 209536.0
         self.A4_dim= "Mill. EUR"
         self.A5= 695144.0
         self.A5_dim= "Mill. EUR"
         self.A6= 0.128056276726
         self.A6_dim= "%"
         self.A7= 0.1664
         self.A7_dim= "%"
         self.A8= 0.135423
         self.A8_dim= "%"
         self.A9= 0.0462
         self.A9_dim= "%"
         self.A10= 0.0331233324557
         self.A10_dim= "%"
         self.A11= 0.438755495507
         self.A11_dim= "%"
         self.A12= 0.0036
         self.A12_dim= "%"
         self.B1= 0.128056276726
         self.B1_dim= "%"
         self.B2= -77.8
         self.B2_dim= "Basis Points Change"
         self.B3= 0.120276276726
         self.B3_dim= "%"
         self.B4= -83.0189851755
         self.B4_dim= "Basis Points Change"
         self.B5= 0.111974378208
         self.B5_dim= "%"
         self.B6= -367.319457091
         self.B6_dim= "Basis Points Change"
         self.B7= 0.0835443310167
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= -158.0
         self.C7= 0.0

#NL-RBS-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'NLRBS', '', u'The Royal Bank of Scotland N.V.', '', '', '', '', '', '', '']


class entityNLRBS(CAResult):
     def __init__(self):
         self.shortname = "NLRBS"
         self.origin = "NL-RBS-CA-DISCLOSURE.xls"
         self.country = "NL"
         self.bank_specific_notes = "-"
         self.A1= 45740.0
         self.A1_dim= "Mill. EUR"
         self.A2= -1528.0
         self.A2_dim= "Mill. EUR"
         self.A3= 3227.0228
         self.A3_dim= "Mill. EUR"
         self.A4= 22203.0
         self.A4_dim= "Mill. EUR"
         self.A5= 56704.0
         self.A5_dim= "Mill. EUR"
         self.A6= 0.145341746611
         self.A6_dim= "%"
         self.A7= 0.2323
         self.A7_dim= "%"
         self.A8= 0.204832
         self.A8_dim= "%"
         self.A9= 0.0765
         self.A9_dim= "%"
         self.A10= 0.0121
         self.A10_dim= "%"
         self.A11= 0.65
         self.A11_dim= "%"
         self.A12= 0.00776125929165
         self.A12_dim= "%"
         self.B1= 0.145341746611
         self.B1_dim= "%"
         self.B2= -1.97
         self.B2_dim= "Basis Points Change"
         self.B3= 0.145144746611
         self.B3_dim= "%"
         self.B4= -123.25574597
         self.B4_dim= "Basis Points Change"
         self.B5= 0.132819172014
         self.B5_dim= "%"
         self.B6= -735.042758643
         self.B6_dim= "Basis Points Change"
         self.B7= 0.0716404707465
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 139.476358
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#NL-SNS-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'NLSNS', '', u'SNS Bank N.V.', '', '', '', '', '', '', '']


class entityNLSNS(CAResult):
     def __init__(self):
         self.shortname = "NLSNS"
         self.origin = "NL-SNS-CA-DISCLOSURE.xls"
         self.country = "NL"
         self.bank_specific_notes = "-"
         self.A1= 74537.0
         self.A1_dim= "Mill. EUR"
         self.A2= -1352.0
         self.A2_dim= "Mill. EUR"
         self.A3= 2299.084662
         self.A3_dim= "Mill. EUR"
         self.A4= 14842.38
         self.A4_dim= "Mill. EUR"
         self.A5= 73727.313349
         self.A5_dim= "Mill. EUR"
         self.A6= 0.1549
         self.A6_dim= "%"
         self.A7= 0.1657
         self.A7_dim= "%"
         self.A8= 0.165686
         self.A8_dim= "%"
         self.A9= 0.0311927594339
         self.A9_dim= "%"
         self.A10= 0.0229
         self.A10_dim= "%"
         self.A11= 0.24
         self.A11_dim= "%"
         self.A12= 0.000147577713082
         self.A12_dim= "%"
         self.B1= 0.1549
         self.B1_dim= "%"
         self.B2= -57.23
         self.B2_dim= "Basis Points Change"
         self.B3= 0.149177
         self.B3_dim= "%"
         self.B4= 4.43207589075
         self.B4_dim= "Basis Points Change"
         self.B5= 0.149620207589
         self.B5_dim= "%"
         self.B6= -812.860851489
         self.B6_dim= "Basis Points Change"
         self.B7= 0.0678909148511
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#PT-BCP-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'PTBCP', '', u'Banco Comercial Portugu\xeas, SA', '', '', '', '', '', '', '']


class entityPTBCP(CAResult):
     def __init__(self):
         self.shortname = "PTBCP"
         self.origin = "PT-BCP-CA-DISCLOSURE.xls"
         self.country = "PT"
         self.bank_specific_notes = "-"
         self.A1= 82006.0
         self.A1_dim= "Mill. EUR"
         self.A2= -740.0
         self.A2_dim= "Mill. EUR"
         self.A3= 5569.403766
         self.A3_dim= "Mill. EUR"
         self.A4= 45559.280456
         self.A4_dim= "Mill. EUR"
         self.A5= 84801.0
         self.A5_dim= "Mill. EUR"
         self.A6= 0.122245209105
         self.A6_dim= "%"
         self.A7= 0.128539
         self.A7_dim= "%"
         self.A8= 0.137511
         self.A8_dim= "%"
         self.A9= 0.06261
         self.A9_dim= "%"
         self.A10= 0.154592810069
         self.A10_dim= "%"
         self.A11= 0.253520339621
         self.A11_dim= "%"
         self.A12= 0.0234
         self.A12_dim= "%"
         self.B1= 0.122245209105
         self.B1_dim= "%"
         self.B2= -196.72
         self.B2_dim= "Basis Points Change"
         self.B3= 0.102573209105
         self.B3_dim= "%"
         self.B4= -142.023458542
         self.B4_dim= "Basis Points Change"
         self.B5= 0.0883708632505
         self.B5_dim= "%"
         self.B6= -726.63877048
         self.B6_dim= "Basis Points Change"
         self.B7= 0.0299093320566
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 250.90877048
         self.B11= 250.90877048
         self.C1= 2242.0
         self.C2= -2250.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#PT-BPI-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'PTBPI', '', u'Banco BPI, SA', '', '', '', '', '', '', '']


class entityPTBPI(CAResult):
     def __init__(self):
         self.shortname = "PTBPI"
         self.origin = "PT-BPI-CA-DISCLOSURE.xls"
         self.country = "PT"
         self.bank_specific_notes = "-"
         self.A1= 40025.320086
         self.A1_dim= "Mill. EUR"
         self.A2= 66.838864
         self.A2_dim= "Mill. EUR"
         self.A3= 3317.327461
         self.A3_dim= "Mill. EUR"
         self.A4= 21710.532156
         self.A4_dim= "Mill. EUR"
         self.A5= 44210.1368659
         self.A5_dim= "Mill. EUR"
         self.A6= 0.152798072252
         self.A6_dim= "%"
         self.A7= 0.161907
         self.A7_dim= "%"
         self.A8= 0.165429
         self.A8_dim= "%"
         self.A9= 0.0762110145078
         self.A9_dim= "%"
         self.A10= 0.062573963804
         self.A10_dim= "%"
         self.A11= 0.433238729539
         self.A11_dim= "%"
         self.A12= 0.074745064325
         self.A12_dim= "%"
         self.B1= 0.152798072252
         self.B1_dim= "%"
         self.B2= -12.26
         self.B2_dim= "Basis Points Change"
         self.B3= 0.151572072252
         self.B3_dim= "%"
         self.B4= -24.4426930938
         self.B4_dim= "Basis Points Change"
         self.B5= 0.149127802943
         self.B5_dim= "%"
         self.B6= -355.907470695
         self.B6_dim= "Basis Points Change"
         self.B7= 0.115981325182
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 113.0
         self.C2= -920.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#PT-CGD-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'PTCGD', '', u'Caixa Geral de Dep\xf3sitos, SA', '', '', '', '', '', '', '']


class entityPTCGD(CAResult):
     def __init__(self):
         self.shortname = "PTCGD"
         self.origin = "PT-CGD-CA-DISCLOSURE.xls"
         self.country = "PT"
         self.bank_specific_notes = "-"
         self.A1= 101506.221252
         self.A1_dim= "Mill. EUR"
         self.A2= -560.0
         self.A2_dim= "Mill. EUR"
         self.A3= 6929.289789
         self.A3_dim= "Mill. EUR"
         self.A4= 63885.076107
         self.A4_dim= "Mill. EUR"
         self.A5= 107793.0
         self.A5_dim= "Mill. EUR"
         self.A6= 0.108464921876
         self.A6_dim= "%"
         self.A7= 0.113188
         self.A7_dim= "%"
         self.A8= 0.094
         self.A8_dim= "%"
         self.A9= 0.063
         self.A9_dim= "%"
         self.A10= 0.164560035087
         self.A10_dim= "%"
         self.A11= 0.231060490205
         self.A11_dim= "%"
         self.A12= 0.0318857841983
         self.A12_dim= "%"
         self.B1= 0.108464921876
         self.B1_dim= "%"
         self.B2= -44.04
         self.B2_dim= "Basis Points Change"
         self.B3= 0.104060921876
         self.B3_dim= "%"
         self.B4= -100.814084762
         self.B4_dim= "Basis Points Change"
         self.B5= 0.0939795134
         self.B5_dim= "%"
         self.B6= -431.998485912
         self.B6_dim= "Basis Points Change"
         self.B7= 0.060861073285
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#SI-NKBM-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'SINKBM', '', u'Nova Kreditna Banka Maribor d.d.', '', '', '', '', '', '', '']


class entitySINKBM(CAResult):
     def __init__(self):
         self.shortname = "SINKBM"
         self.origin = "SI-NKBM-CA-DISCLOSURE.xls"
         self.country = "SI"
         self.bank_specific_notes = "The impact on 2014 of the restructuring measures already taken to improve structural profitability and the maintenance of retained earnings in banks will cover the shortfalls identified"
         self.A1= 4810.79
         self.A1_dim= "Mill. EUR"
         self.A2= -684.91
         self.A2_dim= "Mill. EUR"
         self.A3= 542.9035
         self.A3_dim= "Mill. EUR"
         self.A4= 2777.0
         self.A4_dim= "Mill. EUR"
         self.A5= 5760.36
         self.A5_dim= "Mill. EUR"
         self.A6= 0.1955
         self.A6_dim= "%"
         self.A7= None
         self.A7_dim= "%"
         self.A8= 0.180611
         self.A8_dim= "%"
         self.A9= 0.0942
         self.A9_dim= "%"
         self.A10= 0.194689598736
         self.A10_dim= "%"
         self.A11= 0.686676898196
         self.A11_dim= "%"
         self.A12= 0.000658935434721
         self.A12_dim= "%"
         self.B1= 0.1955
         self.B1_dim= "%"
         self.B2= -389.12
         self.B2_dim= "Basis Points Change"
         self.B3= 0.156588
         self.B3_dim= "%"
         self.B4= -281.357979176
         self.B4_dim= "Basis Points Change"
         self.B5= 0.128452202082
         self.B5_dim= "%"
         self.B6= -1125.80884247
         self.B6_dim= "Basis Points Change"
         self.B7= 0.0440071157531
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 109.928842469
         self.B11= 109.928842469
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#SI-NLB-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'SINLB', '', u'Nova Ljubljanska banka d. d., Ljubljana', '', '', '', '', '', '', '']


class entitySINLB(CAResult):
     def __init__(self):
         self.shortname = "SINLB"
         self.origin = "SI-NLB-CA-DISCLOSURE.xls"
         self.country = "SI"
         self.bank_specific_notes = "The impact on 2014 of the restructuring measures already taken to improve structural profitability and the maintenance of retained earnings in banks will cover the shortfalls identified"
         self.A1= 12535.0
         self.A1_dim= "Mill. EUR"
         self.A2= -1440.0
         self.A2_dim= "Mill. EUR"
         self.A3= 1170.9456
         self.A3_dim= "Mill. EUR"
         self.A4= 7282.0
         self.A4_dim= "Mill. EUR"
         self.A5= 15951.0
         self.A5_dim= "Mill. EUR"
         self.A6= 0.1608
         self.A6_dim= "%"
         self.A7= 0.1494
         self.A7_dim= "%"
         self.A8= 0.149354
         self.A8_dim= "%"
         self.A9= 0.0716
         self.A9_dim= "%"
         self.A10= 0.2325
         self.A10_dim= "%"
         self.A11= 0.7089
         self.A11_dim= "%"
         self.A12= 0.0499
         self.A12_dim= "%"
         self.B1= 0.1608
         self.B1_dim= "%"
         self.B2= -151.16
         self.B2_dim= "Basis Points Change"
         self.B3= 0.145684
         self.B3_dim= "%"
         self.B4= -177.843536028
         self.B4_dim= "Basis Points Change"
         self.B5= 0.127899646397
         self.B5_dim= "%"
         self.B6= -953.581375355
         self.B6_dim= "Basis Points Change"
         self.B7= 0.0503258624645
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 46.7413753555
         self.B11= 46.7413753555
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#SI-SID-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'SISID', '', u'SID - Slovenska izvozna in razvojna banka, d.d., Ljubljana', '', '', '', '', '', '', '']


class entitySISID(CAResult):
     def __init__(self):
         self.shortname = "SISID"
         self.origin = "SI-SID-CA-DISCLOSURE.xls"
         self.country = "SI"
         self.bank_specific_notes = "-"
         self.A1= 3882.1
         self.A1_dim= "Mill. EUR"
         self.A2= 8.7
         self.A2_dim= "Mill. EUR"
         self.A3= 354.46067
         self.A3_dim= "Mill. EUR"
         self.A4= 1462.9
         self.A4_dim= "Mill. EUR"
         self.A5= 3892.8
         self.A5_dim= "Mill. EUR"
         self.A6= 0.2423
         self.A6_dim= "%"
         self.A7= 0.16118
         self.A7_dim= "%"
         self.A8= 0.16118
         self.A8_dim= "%"
         self.A9= 0.0911528826899
         self.A9_dim= "%"
         self.A10= 0.109543413628
         self.A10_dim= "%"
         self.A11= 0.56053046786
         self.A11_dim= "%"
         self.A12= 0.0
         self.A12_dim= "%"
         self.B1= 0.2423
         self.B1_dim= "%"
         self.B2= -139.52
         self.B2_dim= "Basis Points Change"
         self.B3= 0.228348
         self.B3_dim= "%"
         self.B4= 96.3714828746
         self.B4_dim= "Basis Points Change"
         self.B5= 0.237985148287
         self.B5_dim= "%"
         self.B6= -838.242737667
         self.B6_dim= "Basis Points Change"
         self.B7= 0.144523726233
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#SK-SSS-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'SKSSS', '', u'Slovensk\xe1 sporite\u013e\u0148a, a.s.', '', '', '', '', '', '', '']


class entitySKSSS(CAResult):
     def __init__(self):
         self.shortname = "SKSSS"
         self.origin = "SK-SSS-CA-DISCLOSURE.xls"
         self.country = "SK"
         self.bank_specific_notes = "-"
         self.A1= 11678.0
         self.A1_dim= "Mill. EUR"
         self.A2= 189.0
         self.A2_dim= "Mill. EUR"
         self.A3= 973.364
         self.A3_dim= "Mill. EUR"
         self.A4= 4749.8205
         self.A4_dim= "Mill. EUR"
         self.A5= 12502.0
         self.A5_dim= "Mill. EUR"
         self.A6= 0.204926480906
         self.A6_dim= "%"
         self.A7= 0.207725
         self.A7_dim= "%"
         self.A8= 0.207725
         self.A8_dim= "%"
         self.A9= 0.0789
         self.A9_dim= "%"
         self.A10= 0.0457740965402
         self.A10_dim= "%"
         self.A11= 0.689437307542
         self.A11_dim= "%"
         self.A12= 0.0041
         self.A12_dim= "%"
         self.B1= 0.204926480906
         self.B1_dim= "%"
         self.B2= -99.95
         self.B2_dim= "Basis Points Change"
         self.B3= 0.194931480906
         self.B3_dim= "%"
         self.B4= 41.6507921684
         self.B4_dim= "Basis Points Change"
         self.B5= 0.199096560123
         self.B5_dim= "%"
         self.B6= 1.79931426325
         self.B6_dim= "Basis Points Change"
         self.B7= 0.195111412332
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= -0.75

#SK-TB-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'SKTB', '', u'Tatra banka, a.s.', '', '', '', '', '', '', '']


class entitySKTB(CAResult):
     def __init__(self):
         self.shortname = "SKTB"
         self.origin = "SK-TB-CA-DISCLOSURE.xls"
         self.country = "SK"
         self.bank_specific_notes = "-"
         self.A1= 9468.56
         self.A1_dim= "Mill. EUR"
         self.A2= 97.17
         self.A2_dim= "Mill. EUR"
         self.A3= 828.37275
         self.A3_dim= "Mill. EUR"
         self.A4= 5370.318
         self.A4_dim= "Mill. EUR"
         self.A5= 12579.65
         self.A5_dim= "Mill. EUR"
         self.A6= 0.154250223171
         self.A6_dim= "%"
         self.A7= 0.154378
         self.A7_dim= "%"
         self.A8= 0.154378
         self.A8_dim= "%"
         self.A9= 0.0661
         self.A9_dim= "%"
         self.A10= 0.0335620990079
         self.A10_dim= "%"
         self.A11= 0.577226328142
         self.A11_dim= "%"
         self.A12= 6.61135378558e-05
         self.A12_dim= "%"
         self.B1= 0.154250223171
         self.B1_dim= "%"
         self.B2= -54.91
         self.B2_dim= "Basis Points Change"
         self.B3= 0.148759223171
         self.B3_dim= "%"
         self.B4= -8.11020258124
         self.B4_dim= "Basis Points Change"
         self.B5= 0.147948202913
         self.B5_dim= "%"
         self.B6= -319.35854513
         self.B6_dim= "Basis Points Change"
         self.B7= 0.116823368658
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0

#SK-VUB-CA-DISCLOSURE.xls
#
# ['', '', '', u'NAME OF THE ENTITY', '', '', u'SKVUB', '', u'V\u0161eobecn\xe1 \xfaverov\xe1 banka, a.s.', '', '', '', '', '', '', '']


class entitySKVUB(CAResult):
     def __init__(self):
         self.shortname = "SKVUB"
         self.origin = "SK-VUB-CA-DISCLOSURE.xls"
         self.country = "SK"
         self.bank_specific_notes = "-"
         self.A1= 11556.0
         self.A1_dim= "Mill. EUR"
         self.A2= 135.0
         self.A2_dim= "Mill. EUR"
         self.A3= 1115.5225
         self.A3_dim= "Mill. EUR"
         self.A4= 6968.83
         self.A4_dim= "Mill. EUR"
         self.A5= 12993.449
         self.A5_dim= "Mill. EUR"
         self.A6= 0.160073139968
         self.A6_dim= "%"
         self.A7= 0.158361
         self.A7_dim= "%"
         self.A8= 0.158361
         self.A8_dim= "%"
         self.A9= 0.0766
         self.A9_dim= "%"
         self.A10= 0.0378012096069
         self.A10_dim= "%"
         self.A11= 0.487402733823
         self.A11_dim= "%"
         self.A12= 0.0
         self.A12_dim= "%"
         self.B1= 0.160073139968
         self.B1_dim= "%"
         self.B2= -24.86
         self.B2_dim= "Basis Points Change"
         self.B3= 0.157587139968
         self.B3_dim= "%"
         self.B4= 16.4039080875
         self.B4_dim= "Basis Points Change"
         self.B5= 0.159227530776
         self.B5_dim= "%"
         self.B6= -193.431795947
         self.B6_dim= "Basis Points Change"
         self.B7= 0.138243960373
         self.B7_dim= "%"
         self.B8= 0.0
         self.B9= 0.0
         self.B10= 0.0
         self.B11= 0
         self.C1= 0.0
         self.C2= 0.0
         self.C3= 0.0
         self.C4= 0.0
         self.C5= 0.0
         self.C6= 0.0
         self.C7= 0.0


# AT-BAWA
# AT-ERST
# AT-RANI
# AT-RAZE
# AT-VBH
# BE-ABIG
# BE-AXA
# BE-BELF
# BE-BNY
# BE-DXIA
# BE-KBC
# CY-BOCG
# CY-CCBL
# CY-HB
# CY-RCB
# DE-AAB
# DE-APAE
# DE-BLB
# DE-COMM
# DE-DEBK
# DE-DEKA
# DE-DZB
# DE-HASP
# DE-HSH
# DE-HYMU
# DE-HYRE
# DE-IKB
# DE-KFW
# DE-LBB
# DE-LBW
# DE-LHTG
# DE-LKBW
# DE-LWREB
# DE-NLG
# DE-NRW
# DE-SEB
# DE-VWFS
# DE-WGZ
# EE-DP
# EE-SB
# EE-SEB
# ES-BANK
# ES-BBVA
# ES-BKT
# ES-BMN
# ES-BSAB
# ES-CAJAM
# ES-CX
# ES-IBER
# ES-KTXB
# ES-KXA
# ES-LIBER
# ES-NCG
# ES-POPU
# ES-SAN
# ES-UNICN
# FI-DBK
# FI-NBF
# FI-POPO
# FR-BCC
# FR-BNPP
# FR-BPCE
# FR-BPI
# FR-CAGR
# FR-CMUT
# FR-CRH
# FR-HSBC
# FR-LBP
# FR-PSA
# FR-RCIB
# FR-SFL
# FR-SOCG
# GR-ALPH
# GR-EURO
# GR-NBG
# GR-PIRE
# IE-AIB
# IE-BAML
# IE-BIRE
# IE-PTSB
# IE-UBIL
# IT-BAPO
# IT-BPER
# IT-BPM
# IT-BPS
# IT-BPV
# IT-CARI
# IT-CRED
# IT-CRVA
# IT-ICCH
# IT-ISP
# IT-MDB
# IT-UBI
# IT-UCG
# IT-VENE
# LT-DNBB
# LT-SEBB
# LT-SWBK
# LU-BCEE
# LU-CLST
# LU-PCAP
# LU-RBC
# LU-STST
# LU-UBS
# LV-ABLV
# LV-SEB
# LV-SWED
# MT-CBOV
# MT-CHSBC
# MT-DB
# NL-ABN
# NL-GEM
# NL-ING
# NL-NWNV
# NL-RABO
# NL-RBS
# NL-SNS
# PT-BCP
# PT-BPI
# PT-CGD
# SI-NKBM
# SI-NLB
# SI-SID
# SK-SSS
# SK-TB
# SK-VUB


generateAll = [entityATBAWA(),
entityATERST(),
entityATRANI(),
entityATRAZE(),
entityATVBH(),
entityBEABIG(),
entityBEAXA(),
entityBEBELF(),
entityBEBNY(),
entityBEDXIA(),
entityBEKBC(),
entityCYBOCG(),
entityCYCCBL(),
entityCYHB(),
entityCYRCB(),
entityDEAAB(),
entityDEAPAE(),
entityDEBLB(),
entityDECOMM(),
entityDEDEBK(),
entityDEDEKA(),
entityDEDZB(),
entityDEHASP(),
entityDEHSH(),
entityDEHYMU(),
entityDEHYRE(),
entityDEIKB(),
entityDEKFW(),
entityDELBB(),
entityDELBW(),
entityDELHTG(),
entityDELKBW(),
entityDELWREB(),
entityDENLG(),
entityDENRW(),
entityDESEB(),
entityDEVWFS(),
entityDEWGZ(),
entityEEDP(),
entityEESB(),
entityEESEB(),
entityESBANK(),
entityESBBVA(),
entityESBKT(),
entityESBMN(),
entityESBSAB(),
entityESCAJAM(),
entityESCX(),
entityESIBER(),
entityESKTXB(),
entityESKXA(),
entityESLIBER(),
entityESNCG(),
entityESPOPU(),
entityESSAN(),
entityESUNICN(),
entityFIDBK(),
entityFINBF(),
entityFIPOPO(),
entityFRBCC(),
entityFRBNPP(),
entityFRBPCE(),
entityFRBPI(),
entityFRCAGR(),
entityFRCMUT(),
entityFRCRH(),
entityFRHSBC(),
entityFRLBP(),
entityFRPSA(),
entityFRRCIB(),
entityFRSFL(),
entityFRSOCG(),
entityGRALPH(),
entityGREURO(),
entityGRNBG(),
entityGRPIRE(),
entityIEAIB(),
entityIEBAML(),
entityIEBIRE(),
entityIEPTSB(),
entityIEUBIL(),
entityITBAPO(),
entityITBPER(),
entityITBPM(),
entityITBPS(),
entityITBPV(),
entityITCARI(),
entityITCRED(),
entityITCRVA(),
entityITICCH(),
entityITISP(),
entityITMDB(),
entityITMPS(),
entityITUBI(),
entityITUCG(),
entityITVENE(),
entityLTDNBB(),
entityLTSEBB(),
entityLTSWBK(),
entityLUBCEE(),
entityLUCLST(),
entityLUPCAP(),
entityLURBC(),
entityLUSTST(),
entityLUUBS(),
entityLVABLV(),
entityLVSEB(),
entityLVSWED(),
entityMTCBOV(),
entityMTCHSBC(),
entityMTDB(),
entityNLABN(),
entityNLGEM(),
entityNLING(),
entityNLNWNV(),
entityNLRABO(),
entityNLRBS(),
entityNLSNS(),
entityPTBCP(),
entityPTBPI(),
entityPTCGD(),
entitySINKBM(),
entitySINLB(),
entitySISID(),
entitySKSSS(),
entitySKTB(),
entitySKVUB(),]
         

        
        

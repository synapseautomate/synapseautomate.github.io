#!/usr/bin/env python3
import argparse

def calc(cases, minutes, loaded_hourly_cost, monthly_error_impact, correction_minutes, model_ops_cost, pilot_price):
    baseline_time_cost=cases*minutes/60*loaded_hourly_cost
    baseline=baseline_time_cost+monthly_error_impact
    after_time_cost=cases*correction_minutes/60*loaded_hourly_cost
    after=after_time_cost+model_ops_cost
    monthly_net=baseline-after
    annual_conservative=max(0,monthly_net*12*0.70)
    first3=max(0,monthly_net*3)
    return {
      "baseline_monthly_value":round(baseline,2),"after_monthly_cost":round(after,2),"net_monthly_value":round(monthly_net,2),
      "annual_conservative_value":round(annual_conservative,2),"pilot_band_5_10pct_annual":[round(annual_conservative*.05,2),round(annual_conservative*.10,2)],
      "pilot_band_15_25pct_first3":[round(first3*.15,2),round(first3*.25,2)],"pilot_price":pilot_price,"negative_margin_warning":pilot_price < model_ops_cost
    }
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--cases',type=float,required=True);p.add_argument('--minutes',type=float,required=True);p.add_argument('--loaded-hourly-cost',type=float,required=True);p.add_argument('--monthly-error-impact',type=float,default=0);p.add_argument('--correction-minutes',type=float,required=True);p.add_argument('--model-ops-cost',type=float,required=True);p.add_argument('--pilot-price',type=float,required=True);a=p.parse_args();print(calc(a.cases,a.minutes,a.loaded_hourly_cost,a.monthly_error_impact,a.correction_minutes,a.model_ops_cost,a.pilot_price))

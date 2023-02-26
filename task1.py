Oil_work_price = 500
Oil_work_time = 0.7
Oil_work_cost = Oil_work_price*Oil_work_time
Oil_price = 700*1.05
filtr_work_price = 450
filtr_work_time = 0.5
filtr_work_cost = filtr_work_price*filtr_work_time
filtr_price = 300*1.05
cost_sum = Oil_work_cost + Oil_price + filtr_work_cost + filtr_price
personaldiscount = 3 # персональная скидка клиента в процентах от стоимости "ИТОГО" калькуляции.  
Net_sum_cost = cost_sum*0.97 # 0.97 является фактическим дисконтом стоимости "ИТОГО" калькуляции по осмотру автомобиля и обЪему планируемых работ с учетом персональной скидки клиента в размере 3% от стоимости калькуляции. 

print("""
      Расчет работ по предоставленному автомобилю:
          Замена масла (работы) {} руб.
          Масло Castrol {} руб.
          Замена воздушного фильтра (работы) {} руб.
          Воздушный фильтр {} руб.
          Итого {} руб.
          Персональная скидка {}%.
          Итого с учетом скидки {} руб.
          Спасибо что выбираете нас!
          """.format(Oil_work_cost, Oil_price, filtr_work_cost, filtr_price, cost_sum, personaldiscount, Net_sum_cost ))


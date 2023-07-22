# Proyecto Parte 2

![](https://www.diarioeldia.cl/u/fotografias/fotosnoticias/2019/11/8/67218.jpg)

**Giturra**, un banquero astuto y ambicioso, estableció su propio banco con el objetivo de obtener enormes ganancias. Sin embargo, su reputación se vio empañada debido a las tasas de interés usureras que imponía a sus clientes. A medida que su banco crecía, Giturra enfrentaba una creciente cantidad de préstamos impagados, lo que amenazaba su negocio y su prestigio.

Para abordar este desafío, Giturra reconoció la necesidad de reducir los riesgos de préstamo y mejorar la calidad de los préstamos otorgados. Decidió aprovechar la ciencia de datos y el análisis de riesgo crediticio. Contrató a un equipo de expertos para desarrollar un modelo predictivo de riesgo crediticio.

Cabe señalar que lo modelos solicitados por el banquero deben ser interpretables. Ya que estos le permitira al equipo comprender y explicar cómo se toman las decisiones crediticias. Utilizando visualizaciones claras y explicaciones detalladas, pudieron identificar las características más relevantes, le permitirá analizar la distribución de la importancia de las variables y evaluar si los modelos son coherentes con el negocio.

Para esto Giturra les solicita crear un modelo de riesgo disponibilizandoles una amplia gama de variables de sus usuarios: como historiales de crédito, ingresos y otros factores financieros relevantes, para evaluar la probabilidad de incumplimiento de pago de los clientes. Con esta información, Giturra podra tomar decisiones más informadas en cuanto a los préstamos, ofreciendo condiciones más favorables a aquellos con menor riesgo de impago.

---
Para el desarrollo de su proyecto, utilice el conjunto de datos `dataset.pq` para entrenar un modelo de su elección. Además, se adjunta junto con los datos del proyecto un archivo llamado `requirements.txt` que contiene todas las bibliotecas y versiones necesarias para el desarrollo del proyecto. Se le recomienda levantar un ambiente de `conda` para instalar estas librerías y así evitar cualquier problema con las versiones.

---

### Descripción variables

- Age: Representa la edad de la persona
- Annual_Income: Representa el ingreso anual de la persona
- Monthly_Inhand_Salary: Representa el salario mensual base de una persona
- Num_Bank_Accounts: Representa el número de cuentas bancarias que tiene una persona
- Num_Credit_Card: Representa el número de otras tarjetas de crédito que tiene una persona
- Interest_Rate: Representa la tasa de interés de la tarjeta de crédito (porcentaje)
- Num_of_Loan: Representa el número de préstamos tomados del banco
- Delay_from_due_date: Representa el número promedio de días de retraso en la fecha de pago (días)
- Num_of_Delayed_Payment: Representa el número promedio de pagos retrasados por una persona
- Changed_Credit_Limit: Representa el cambio porcentual en el límite de la tarjeta de crédito (porcentaje)
- Num_Credit_Inquiries: Representa el número de consultas de tarjetas de crédito
- Credit_Mix: Representa la clasificación de la mezcla de créditos (Malo, Estándar, Bueno)
- Outstanding_Debt: Representa la deuda pendiente por pagar
- Credit_Utilization_Ratio: Representa la proporción de utilización de la tarjeta de crédito (porcentaje)
- Credit_History_Age: Representa la antigüedad del historial crediticio de la persona (días)
- Payment_of_Min_Amount: Representa si la persona pagó solo el monto mínimo
- Total_EMI_per_month: Representa los pagos mensuales de las cuotas de préstamos
- Amount_invested_monthly: Representa la cantidad invertida mensualmente por el cliente
- Monthly_Balance: Representa el monto del saldo mensual del cliente
- Credit_Score: 1 Si el cliente es riesgoso y 0 sino
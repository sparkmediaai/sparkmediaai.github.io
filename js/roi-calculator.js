document.addEventListener('DOMContentLoaded', () => {
  const inputs = {
    platform: document.querySelector('[data-field="platform"]'),
    aiPerLead: document.querySelector('[data-field="ai-per-lead"]'),
    costPerLead: document.querySelector('[data-field="cost-per-lead"]'),
    leadsPerMonth: document.querySelector('[data-field="leads-per-month"]'),
    closeRate: document.querySelector('[data-field="close-rate"]'),
    avgCommission: document.querySelector('[data-field="avg-commission"]')
  };

  const outputs = {
    totalLeadCost: document.querySelector('[data-output="total-lead-cost"]'),
    numberOfSales: document.querySelector('[data-output="number-of-sales"]'),
    commissionRevenue: document.querySelector('[data-output="commission-revenue"]'),
    totalMonthlyCost: document.querySelector('[data-output="total-monthly-cost"]'),
    netProfit: document.querySelector('[data-output="net-profit"]'),
    roi: document.querySelector('[data-output="roi"]')
  };

  const currencyFormatter = new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD',
    maximumFractionDigits: 0
  });

  const numberFormatter = new Intl.NumberFormat('en-US', {
    maximumFractionDigits: 1
  });

  const percentFormatter = new Intl.NumberFormat('en-US', {
    style: 'percent',
    minimumFractionDigits: 1,
    maximumFractionDigits: 1
  });

  function toNumber(input) {
    return input ? parseFloat(input.value) || 0 : 0;
  }

  function recalc() {
    const platformCost = toNumber(inputs.platform);
    const aiCostPerLead = toNumber(inputs.aiPerLead);
    const leadCost = toNumber(inputs.costPerLead);
    const leads = toNumber(inputs.leadsPerMonth);
    const closeRatePercent = toNumber(inputs.closeRate);
    const closeRate = closeRatePercent / 100;
    const avgCommission = toNumber(inputs.avgCommission);

    const totalLeadCost = (leadCost + aiCostPerLead) * leads;
    const numberOfSales = leads * closeRate;
    const commissionRevenue = avgCommission * leads * closeRate;
    const totalMonthlyCost = totalLeadCost + platformCost;
    const netProfit = commissionRevenue - totalMonthlyCost;
    const roi = totalMonthlyCost > 0 ? netProfit / totalMonthlyCost : 0;

    if (outputs.totalLeadCost) outputs.totalLeadCost.textContent = currencyFormatter.format(totalLeadCost);
    if (outputs.numberOfSales) outputs.numberOfSales.textContent = numberFormatter.format(numberOfSales);
    if (outputs.commissionRevenue) outputs.commissionRevenue.textContent = currencyFormatter.format(commissionRevenue);
    if (outputs.totalMonthlyCost) outputs.totalMonthlyCost.textContent = currencyFormatter.format(totalMonthlyCost);
    if (outputs.netProfit) {
      outputs.netProfit.textContent = currencyFormatter.format(netProfit);
      outputs.netProfit.parentElement.dataset.positive = netProfit >= 0 ? 'true' : 'false';
    }
    if (outputs.roi) outputs.roi.textContent = percentFormatter.format(roi);
  }

  Object.values(inputs).forEach((input) => {
    if (!input) return;
    input.addEventListener('input', recalc);
    input.addEventListener('change', recalc);
  });

  recalc();
});

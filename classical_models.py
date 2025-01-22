import QuantLib as ql

def calculate_classical_prices():
    # Black-Scholes Model
    spot_price = 100
    strike_price = 100
    maturity = 1
    volatility = 0.2
    risk_free_rate = 0.05
    
    process = ql.BlackScholesMertonProcess(
        ql.QuoteHandle(ql.SimpleQuote(spot_price)),
        ql.YieldTermStructureHandle(ql.FlatForward(0, ql.NullCalendar(), risk_free_rate, ql.Actual360())),
        ql.BlackVolTermStructureHandle(ql.BlackConstantVol(0, ql.NullCalendar(), volatility, ql.Actual360()))
    )
    
    engine = ql.AnalyticEuropeanEngine(process)
    option = ql.VanillaOption(
        ql.PlainVanillaPayoff(ql.Option.Call, strike_price),
        ql.EuropeanExercise(ql.Date(1, ql.January, 2025))
    )
    option.setPricingEngine(engine)
    return {"Black-Scholes": option.NPV()}

init python :
    def cps(sp):
        preferences.text_cps = sp
    
    def dot(amount, cps=preferences.slow_cps):
        return f"{{cps={cps}}}" + "." * amount + "{/cps}"
    
    def cps_str(s, cps):
        return f"{{cps={cps}}}" + str(s) + "{/cps}"
    
    def slow(s):
        return f"{{cps={preferences.slow_cps}}}" + str(s) + "{/cps}"
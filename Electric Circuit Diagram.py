import schemdraw
import schemdraw.elements as elm

with schemdraw.Drawing() as d:
    d += elm.Battery().right()
    d += elm.Resistor().down()
    d += elm.Ground()
    d += elm.Line().left()
    d += elm.Switch().up()
    d += elm.Line().right()

    d.draw()

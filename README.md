# Tutorial basico de PyScript


["PyScript Pagina"](https://pyscript.net/)
["PyScript Documentación"](https://docs.pyscript.net/2024.7.1/beginning-pyscript/)
["PyScript Ejemplos"](https://pyscript.com/@examples)
["PyScript comunidad"](https://discord.com/invite/HxvBtukrg2)


### Servir los archivos con un servidor HTTP
```
  python3 -m http.server
```

## Demo 1  PyScript 2022.12.1

- ["Video tutorial"](https://www.youtube.com/live/AcFSzDBNjkI?si=D7zMcmHQUlpwmYyh)
- ["Guia del tutorial"](https://jeff.glass/post/whats-new-pyscript-2022-12-1/)

- Template html
```
<!DOCTYPE html>
<html>
  <head>
      <meta charset="utf-8" />
      <meta name="viewport" content="width=device-width,initial-scale=1" />
      <title>PyScript Demo 1</title>

      <link rel="stylesheet" href="https://pyscript.net/releases/2022.12.1/pyscript.css">
      <script type="module" src="https://pyscript.net/releases/2022.12.1/pyscript.js"></script>
  </head>
  <body>
        <h1>Demo 1</h1>

        <py-config>
        </py-config>

        <py-script>
        </py-script>
    
  </body>
</html>

```

- Insertar texto en html

```
    <py-script>
        display("Hello")
        display("World")
    </py-script>
    
```

- Insertar texto en html en un elemento
```
    <div id="output"></div>
    <div id="output-2">My Name is: </div>
    <div id="output-3">Country</div>

    <py-config>
    </py-config>

    <py-script>
        display("Hello", target="output")
        display("World!", append=True, target="output")
        display("Wilfredo", append=True, target="output-2")
        display("Costa Rica", append=False, target="output-3")
    </py-script>
```

target: indica el id del elemento objetivo
append: valor booleano, si su valor es true se agrega al contenido existen, si el valor es false reemplaza el contenido existente

![alt text](./img/image-1.png)

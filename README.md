# Tutorial basico de PyScript


1. ["PyScript Pagina"](https://pyscript.net/)
2. ["PyScript Documentación"](https://docs.pyscript.net/2024.7.1/beginning-pyscript/)
3. ["PyScript Ejemplos"](https://pyscript.com/@examples)
4. ["PyScript comunidad"](https://discord.com/invite/HxvBtukrg2)


### Servir los archivos con un servidor HTTP
```
  python3 -m http.server
```

## PyScript 2022.12.1

### Demo 1 - Insertar contenido

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

- `target`: 
indica el id del elemento objetivo
- `append`: 
valor booleano, si su valor es true se agrega al contenido existen, si el valor es false reemplaza el contenido existente

![alt text](./img/image-1.png)

### Demo 2 - py-terminal

- utilizar py-terminal
```
        <h1>Demo 2 - py-terminal</h1>

        <py-config>
        </py-config>

        <py-script>
          print("Hello world!")
          print("My name is Wilfredo.")
        </py-script>
```
`display()` es para escribir en la pantalla, y  `print()` escribe al `<py-terminal>`. 

![alt text](./img/image-2.png)
```
    <py-config>
        terminal = false
    </py-config>
```
Por defecto py-terminal se muestra en pantalla al igual que su contenido, pero es posible configurarlo para que
se muestre en consola.

![alt text](./img/image-3.png)

### Demo 3 - Leer archivos

Esta acción se realiza en la etiqueta `py-config`


- Importar un archivo y leer desde el otro directorio

```
    <py-config>
        [[fetch]]
        files = ['texto.txt']
        from = 'file/'
    </py-config>

    <py-script>
        text = 'Content: '
        with open('texto.txt', 'r') as fp:
            #print(fp.read())
            for line in fp:
                text += f"{line}"
        
        
        display(HTML(f"<p>{text}</p>"))
    </py-script>
```

- Importar un archivo y leer desde el mismo directorio

```
    <py-config>
        [[fetch]]
        files = ['texto2.txt']  
    </py-config>

    <py-script>
        text2 = ''
        with open('texto2.txt', 'r') as fp:
            #print(fp.read())
            for line in fp:
                text2 += f"{line}"
        
        
        display(HTML(f"<p>{text2}</p>"))
    </py-script>
```

`HTML` esta funcion permite insertar etiquetas html junto con su contenido

### Demo 4 - Importar archivos.py con funciones

```
<p id="date"></p>

<py-config>

    [[fetch]]
    files = ['demo4.py'] 
    from ="package"                                                                                                          
</py-config>

<py-script>

    from demo4 import demo4, hello_world, date, show_params,console_message

    print(demo4())

    hello_world()

    date()

    show_params("<h2>Tutorial</h2>")

    console_message("Pura vida!")

</py-script>
```

## PyScript 2024.7.1

En esta version hay muchos cambios considerables

- Cambio de tag para configurar y acceder a archivos
```
   <script type="py" src="./latest/main.py" config="./latest/pyscript.json"></script>
```
Se crea un archivo `main.py` donde escribiremos el codigo en python y otro archivo que contiene la configuracion `pyscript.json`
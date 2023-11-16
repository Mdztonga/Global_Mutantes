# Global_Mutantes
## Nombre y Apellido: Gaston Sisterna
## Legajo: 51648
## Gmail: gastonsisterna30@gmail.com
### Descripcion del codigo:
- El código que he creado utiliza bucles, condiciones y funciones para analizar una secuencia de ADN representada por una matriz. El usuario ingresa una serie de letras (A, T, C, G), que corresponden a las bases nitrogenadas - del ADN. La matriz se llena con estas letras, y luego el programa la recorre en direcciones horizontal, vertical y oblicua.
- Durante el recorrido de la matriz, el programa busca secuencias de cuatro letras consecutivas. Si encuentra más de una de estas secuencias, se incrementará un contador. Si el contador de secuencias es mayor que uno, 
- concluimos que la persona cuya secuencia de ADN estamos analizando es mutante.
### Elaboracion del codigo:
- Primero empece haciendo los bucles para recorrer las matricez de forma vertical, horizontal y oblicua, luego de esto genere contadores para que vayan almacenando las veces que se encontaban
- 4 letras iguales de forma consecurtivas para detectar si es mutante o no.
  
![Captura de pantalla 2023-11-11 011158](https://github.com/Mdztonga/Global_Mutantes/assets/146146598/09eac9aa-a5e5-44e6-9e5b-10e11a20c777)
- Luego de esto me puse a generar con un import de randoms unos bucles que me guardaran solo las letra que se podrian ingresar (A ,T ,C, G)
![Captura de pantalla 2023-11-12 003123](https://github.com/Mdztonga/Global_Mutantes/assets/146146598/3a71bce7-6389-43db-b6e4-e8f7552ef3d0)

- Una vez terminado el codigo me pusea probar que el codigo copilase bien 
![Captura de pantalla 2023-11-12 004557](https://github.com/Mdztonga/Global_Mutantes/assets/146146598/d3225c5c-ec02-4f59-84a5-9cb331502246)

- Y para finalizar decidi implementar una funcion , decorarlo para que el codigo fuese muecho mas entendible, eficiente y bonito
![Captura de pantalla 2023-11-13 223902](https://github.com/Mdztonga/Global_Mutantes/assets/146146598/dfd83ae3-8776-42dd-85f9-6c19aa10e4ed)

### Como se corre el codigo
- Se le pide al usuario que este ingrese una cantidad de letras (36) para poder rellerar la matriz y luego de esto el programa solo va hacerce cargo de definir si es mutante o no
- Se le imprimira por pantalla dicha matriz, si es mutante o no y la cantidad de secuencias que se encontraron en su ADN

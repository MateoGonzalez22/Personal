/*

/////// Resolucion con math ceiling, funciona idealmente solo si los tipos de enemigos son 5 o 10 //////


List<string> tiposDeEnemigos = new List<string>();
tiposDeEnemigos.Add("mago");
tiposDeEnemigos.Add("guerrero");
tiposDeEnemigos.Add("bruja");
tiposDeEnemigos.Add("monstruo");





List<string> todosLosEnemigos = new List<string>();


List<string> DevolverEnemigosListados(List<string> tiposDeEnemigos){

    double res = 50.0/tiposDeEnemigos.Count;

    int cantidadPorCadaTipo = (int)Math.Ceiling(res);

    for(int x = 0; x < tiposDeEnemigos.Count; x++){

        for(int i = 1; i <= cantidadPorCadaTipo; i++){

            if(todosLosEnemigos.Count < 50){
                todosLosEnemigos.Add(tiposDeEnemigos.ElementAt(x) + i);
            }else{
                return todosLosEnemigos;
            }  
        }    
    }


    return todosLosEnemigos;
}*/




//string[] tiposDeEnemigos = {"ladron", "mago", "bruja", "monstruo", "perro", "gato"};

string[] tiposDeEnemigos = {"ladron", "mago"};

List<string> DevolverArrayDeEnemigosListados(string[] tiposDeEnemigos){

    List<string> todosLosEnemigos = new List<string>();
    List<string> todosLosEnemigosEnumerados = new List<string>();


    for(int i = 0; i<50;)
    {
        foreach (string tipo in tiposDeEnemigos)
        {

            if(todosLosEnemigos.Count < 50){
                todosLosEnemigos.Add(tipo);
                i+=1;
            }
   
        }
    }
    


    int x = 1;

    foreach (string tipo in tiposDeEnemigos)
    {
        
        foreach (string enemigo in todosLosEnemigos)
        {
            
            if(tipo == enemigo){

                todosLosEnemigosEnumerados.Add(enemigo + x);
                x+=1;
            }

        }

        x = 1;
    }

    return todosLosEnemigosEnumerados;
}






List<List<string>> DevolverEnemigosOrdenadosPorListas(List<string> todosLosEnemigosEnumerados){

    List<List<string>> todosLosEnemigosOrdenados = new List<List<string>>();
    

    foreach (string tipo in tiposDeEnemigos)
    {
        
        
        List<string> listaDeEnemigos = new List<string>();

        foreach (string enemigo in todosLosEnemigosEnumerados)

        {
            
            if(enemigo.IndexOf(tipo) == 0){

                listaDeEnemigos.Add(enemigo);

            }
        }
        
        todosLosEnemigosOrdenados.Add(listaDeEnemigos);
        
    }
    
    return todosLosEnemigosOrdenados;
}



int i=1;

foreach(List<string> lista in DevolverEnemigosOrdenadosPorListas(DevolverArrayDeEnemigosListados(tiposDeEnemigos))){

    Console.WriteLine("\nLista " + i + "\n");

    foreach (string enemigo in lista)
    {
        Console.WriteLine(enemigo);
    }

    i+=1;

}



/*List<string> hola = Metodo(tiposDeEnemigos);


foreach(string enemy in hola){

    Console.Write(enemy + "\n");
    

}*/



/*string a = "mago";

string b = "mago2";

Console.WriteLine("a.IndexOf(b): " + a.IndexOf(b));
Console.WriteLine("\nb.IndexOf(a): " + b.IndexOf(a));
*/


//Console.WriteLine(i%3);



/*
//Enumera a todos los enemigos sin importar cual son

for(int i = 1; i <= 50; i++){


        enemigos.Add(tiposDeEnemigos.ElementAt(x) + i);


        if (x == 3){
            x = 0;
        }else{
            x+=1;
        }

    }

*/
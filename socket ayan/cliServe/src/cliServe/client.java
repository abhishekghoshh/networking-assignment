

import java.io.IOException;
import java.io.PrintStream;
import java.net.Socket;
import java.net.UnknownHostException;
import java.util.Scanner;

 class client {
	public static void main(String args[]) throws UnknownHostException, IOException {
		int num1,num2,tmp,op;
	Scanner sc=new Scanner(System.in);
	Socket skt=new Socket("127.0.0.1",123);
	Scanner sc1=new Scanner(skt.getInputStream());
	System.out.println("Choose a Option->");
	System.out.println("1.Sum");
	System.out.println("2.Subtract");
	System.out.println("3.Multiply");	
	System.out.println("4.Divide");
	
	op=sc.nextInt();
	
	System.out.println("Enter 2 operands->");
	
	num1=sc.nextInt();
	num2=sc.nextInt();
	
	System.out.println("Enter your current time");
	//String time=sc.next();
	
	PrintStream p=new PrintStream(skt.getOutputStream());
	p.println(num1);
	p.println(num2);
	p.println(op);
	//p.println(time);
	
	tmp=sc1.nextInt();
	System.out.println(tmp);
	
	sc.close();
	skt.close();
	sc1.close();
	
}
}

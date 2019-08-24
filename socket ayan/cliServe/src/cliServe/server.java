

import java.io.IOException;
import java.io.PrintStream;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Scanner;

class server {

	public static void main(String args[]) throws IOException {
		int num1,num2,op,tmp;
		//String time;
		ServerSocket s1=new ServerSocket(123);
		Socket ss=s1.accept();
		Scanner sc=new Scanner(ss.getInputStream());
		
		num1=sc.nextInt();
		num2=sc.nextInt();
		op=sc.nextInt();
		//time=sc.next();
		
		switch(op) {
		case 1:
			tmp=num1+num2;
			break;
		case 2:
			tmp=(num1>num2)?num1-num2:num2-num1;
			break;
		case 3:
			tmp=num1*num2;
			break;
		case 4:
			tmp=(num1>num2)?num1/num2:num2/num1;
			break;
		default:
				tmp=0;
				System.out.println("Wrong operation!!");
		}
		
		
		PrintStream p=new PrintStream(ss.getOutputStream());
		p.println(tmp);
		
		s1.close();
		sc.close();
	}
}

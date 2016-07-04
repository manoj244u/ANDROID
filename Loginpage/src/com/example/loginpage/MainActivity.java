package com.example.loginpage;

import android.R.integer;
import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.Menu;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity extends Activity {
	TextView t1,t2,t3,t4;
	EditText edt1,edt2;
	Button bt;
	int attemptcount =5;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        t4=(TextView)findViewById(R.id.textView4);
        edt1=(EditText)findViewById(R.id.editText1);
        edt2=(EditText)findViewById(R.id.editText2);
        bt=(Button)findViewById(R.id.button1);
        bt.setOnClickListener(new OnClickListener() {
			
			@Override
			public void onClick(View arg0) {
				// TODO Auto-generated method stub
				t4.setText(Integer.toString(attemptcount));
				if(edt1.getText().toString().equals("user") && edt2.getText().toString().equals("p3solutions"))
				{
					Toast.makeText(MainActivity.this, "user name and password is correct", Toast.LENGTH_LONG).show();
				Intent i=new Intent(MainActivity.this,SecondMainActivity.class);
				startActivity(i);
				
				}
				else
				{
					Toast.makeText(MainActivity.this," Wrong credential",Toast.LENGTH_LONG).show();
					attemptcount--;
					t4.setText(Integer.toString(attemptcount));
					if(attemptcount==0)
					{
						bt.setEnabled(false);
					}
				}
			}
		});
    }


    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.main, menu);
        return true;
    }
    
}

public class SignInActivity extends AppCompatActivity {
    EditText etUsername, etPassword;
    Button btnSignIn;
    int loginAttempts = 0;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_signin);

        etUsername = findViewById(R.id.username);
        etPassword = findViewById(R.id.password);
        btnSignIn = findViewById(R.id.signin);

        btnSignIn.setOnClickListener(v -> {
            String username = etUsername.getText().toString();
            String password = etPassword.getText().toString();

            if (username.isEmpty() || password.isEmpty()) {
                Toast.makeText(this, "Fields cannot be empty", Toast.LENGTH_SHORT).show();
            } else if (username.equals(SignUpActivity.savedUsername) && password.equals(SignUpActivity.savedPassword)) {
                Toast.makeText(this, "Sign In Successful", Toast.LENGTH_SHORT).show();
                startActivity(new Intent(this, SuccessActivity.class));
                finish();
            } else {
                loginAttempts++;
                if (loginAttempts > 2) {
                    btnSignIn.setEnabled(false);
                    Toast.makeText(this, "Too many attempts. Try later.", Toast.LENGTH_SHORT).show();
                } else {
                    Toast.makeText(this, "Incorrect credentials", Toast.LENGTH_SHORT).show();
                }
            }
        });
    }
}
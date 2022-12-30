import paramiko

# Crear un cliente SSH
ssh = paramiko.SSHClient()

# Conéctese al host remoto
ssh.connect(hostname="remote.example.com", username="user", password="password")

# Ejecutar un comando en el host remoto
stdin, stdout, stderr = ssh.exec_command("ls -l")

# Imprime la salida del comando
print(stdout.read())

# Cerrar la conexión
ssh.close()
#Este ejemplo se conecta al host remoto remote.example.com usando el nombre de usuario y la contraseña, y luego ejecuta el comando ls -l. La salida del comando se imprime en la consola.

#También puede usar paramiko para transferir archivos entre el host local y el remoto usando la clase SFTPClient.

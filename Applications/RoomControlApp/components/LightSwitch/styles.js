import { StyleSheet } from 'react-native'

const styles = StyleSheet.create({
    container: {
        backgroundColor: '#fff',
        alignItems: 'center',
        justifyContent: 'center',
    },
    buttons: {
        margin: 20,
        padding: 20,
        borderRadius: 10,
        paddingLeft: 80,
        paddingRight: 80,
        borderWidth: 1
    },
    onButton: {
        backgroundColor: '#fff59d',
        borderColor: 'orange'
    },
    offButton: {
        backgroundColor: '#bdbdbd',
        borderColor: 'black'
    }
})

export default styles
